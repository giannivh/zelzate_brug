"""DataUpdateCoordinator for zelzate_brug."""
from __future__ import annotations

from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)
from .api import (
    ZelzateBrugApiClient,
    ZelzateBrugApiClientError,
)
from .const import DOMAIN, LOGGER

type ZelzateBrugConfigEntry = ConfigEntry[ZelzateBrugDataUpdateCoordinator]


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class ZelzateBrugDataUpdateCoordinator(DataUpdateCoordinator[dict]):
    """Class to manage fetching data from the API."""

    config_entry: ZelzateBrugConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        config_entry: ZelzateBrugConfigEntry,
        client: ZelzateBrugApiClient,
    ) -> None:
        """Initialize."""
        self.client = client
        super().__init__(
            hass=hass,
            logger=LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=30),
            config_entry=config_entry,
        )

    async def _async_update_data(self):
        """Update data via library."""
        try:
            result = await self.client.async_get_data()
            LOGGER.debug("Got data: " + str(result))
            return result
        except ZelzateBrugApiClientError as exception:
            raise UpdateFailed(exception) from exception
