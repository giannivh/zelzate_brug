"""Adds config flow for ZelzateBrug."""
from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import (
    ZelzateBrugApiClient,
    ZelzateBrugApiClientCommunicationError,
    ZelzateBrugApiClientError,
)
from .const import DOMAIN, LOGGER, NAME


class ZelzateBrugFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for ZelzateBrug."""

    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle user step."""
        errors = {}
        try:
            await ZelzateBrugApiClient(
                session=async_get_clientsession(self.hass),
            ).async_get_data()
        except ZelzateBrugApiClientCommunicationError as exception:
            LOGGER.debug("Could not reach the bridge status: %s", exception)
            errors["base"] = "cannot_connect"
        except ZelzateBrugApiClientError as exception:
            LOGGER.error("Unexpected bridge status response: %s", exception)
            errors["base"] = "unknown"
        else:
            return self.async_create_entry(title=NAME, data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            errors=errors,
        )
