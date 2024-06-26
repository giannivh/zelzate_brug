"""DataUpdateCoordinator for zelzate_brug."""
from __future__ import annotations

from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.exceptions import ConfigEntryAuthFailed

from .api import (
    ZelzateBrugApiClient,
    ZelzateBrugApiClientAuthenticationError,
    ZelzateBrugApiClientError,
)
from .const import DOMAIN, LOGGER


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class ZelzateBrugDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    config_entry: ConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        client: ZelzateBrugApiClient,
    ) -> None:
        """Initialize."""
        self.client = client
        super().__init__(
            hass=hass,
            logger=LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
        )

    async def _async_update_data(self):
        """Update data via library."""
        try:
            result = await self.client.async_get_data()
            LOGGER.debug("Got data: " + str(result))
            return result
        except ZelzateBrugApiClientAuthenticationError as exception:
            raise ConfigEntryAuthFailed(exception) from exception
        except ZelzateBrugApiClientError as exception:
            raise UpdateFailed(exception) from exception
