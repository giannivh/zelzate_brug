"""API Client."""
from __future__ import annotations

import asyncio
import socket

import aiohttp
import async_timeout

import json


class ZelzateBrugApiClientError(Exception):
    """Exception to indicate a general API error."""


class ZelzateBrugApiClientCommunicationError(
    ZelzateBrugApiClientError
):
    """Exception to indicate a communication error."""


class ZelzateBrugApiClientAuthenticationError(
    ZelzateBrugApiClientError
):
    """Exception to indicate an authentication error."""


class ZelzateBrugApiClient:
    """API Client."""

    def __init__(
        self,
        session: aiohttp.ClientSession,
    ) -> None:
        """Init API Client."""
        self._session = session

    async def async_get_data(self) -> any:
        """Get data from the API."""
        response = await self._api_wrapper(
            method="get", url="https://www.zelzatebrug.vlaanderen"
        )
        response = await self._api_wrapper(
            method="post", url="https://www.zelzatebrug.vlaanderen/request.php", data={"action": "status_json"}
        )
        return json.loads(response)

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> any:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    data=data,
                )
                if response.status in (401, 403):
                    raise ZelzateBrugApiClientAuthenticationError(
                        "Invalid credentials",
                    )
                response.raise_for_status()
                return await response.text()

        except asyncio.TimeoutError as exception:
            raise ZelzateBrugApiClientCommunicationError(
                "Timeout error fetching information",
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            raise ZelzateBrugApiClientCommunicationError(
                "Error fetching information",
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            raise ZelzateBrugApiClientError(
                "Something really wrong happened!"
            ) from exception
