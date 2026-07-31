"""ZelzateBrugEntity class."""
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTRIBUTION, DOMAIN, NAME, VERSION
from .coordinator import ZelzateBrugDataUpdateCoordinator


class ZelzateBrugEntity(CoordinatorEntity[ZelzateBrugDataUpdateCoordinator]):
    """ZelzateBrugEntity class."""

    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name = True

    def __init__(self, coordinator: ZelzateBrugDataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.config_entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self.unique_id)},
            name=NAME,
            sw_version=VERSION,
            manufacturer=NAME,
        )
