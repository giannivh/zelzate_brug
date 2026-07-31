"""API Client."""
from __future__ import annotations

import asyncio
import socket

import aiohttp

import json
import re

from .const import ZB_BASE_URL, ZB_CSRF_TOKEN_PATTERN, ZB_STATUS_PATH


class ZelzateBrugApiClientError(Exception):
    """Exception to indicate a general API error."""


class ZelzateBrugApiClientCommunicationError(
    ZelzateBrugApiClientError
):
    """Exception to indicate a communication error."""


class ZelzateBrugApiClient:
    """API Client."""

    def __init__(
        self,
        session: aiohttp.ClientSession,
    ) -> None:
        """Init API Client."""
        self._session = session

    async def async_get_data(self) -> dict:
        """Get data from the API."""
        page, cookies = await self._api_wrapper(method="get", url=ZB_BASE_URL)
        response, _ = await self._api_wrapper(
            method="post",
            url=ZB_BASE_URL + ZB_STATUS_PATH,
            data={
                "action": "status_json",
                "csrf_token": self._extract_csrf_token(page),
            },
            cookies=cookies,
        )
        try:
            return json.loads(response)
        except json.JSONDecodeError as exception:
            raise ZelzateBrugApiClientError(
                "Malformed response from the status endpoint",
            ) from exception

    @staticmethod
    def _extract_csrf_token(page: str) -> str:
        """Extract the CSRF token from the given homepage."""
        matches = re.search(ZB_CSRF_TOKEN_PATTERN, page, re.IGNORECASE)
        if not matches:
            raise ZelzateBrugApiClientError(
                "No CSRF token found on the homepage",
            )
        return matches.group(1)

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
        cookies: dict | None = None,
    ) -> tuple[str, dict]:
        """Get information from the API, returning its body and the cookies it set."""
        try:
            async with asyncio.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    data=data,
                    cookies=cookies,
                )
                if response.status in (401, 403):
                    raise ZelzateBrugApiClientCommunicationError(
                        "Access denied, the CSRF token or session was rejected",
                    )
                response.raise_for_status()
                return (
                    await response.text(),
                    {name: cookie.value for name, cookie in response.cookies.items()},
                )

        except TimeoutError as exception:
            raise ZelzateBrugApiClientCommunicationError(
                "Timeout error fetching information",
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            raise ZelzateBrugApiClientCommunicationError(
                "Error fetching information",
            ) from exception
        except ZelzateBrugApiClientError:
            raise
        except Exception as exception:  # pylint: disable=broad-except
            raise ZelzateBrugApiClientError(
                "Something really wrong happened!"
            ) from exception
