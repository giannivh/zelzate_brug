"""Sensor platform for zelzate_brug."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from datetime import datetime

from .coordinator import ZelzateBrugDataUpdateCoordinator
from .entity import ZelzateBrugEntity
from .const import (
    DOMAIN, NAME,
    ZB_ICONS, ZB_DEFAULT_ICON,
    ZB_TIME_PATTERN,
    ZB_CODE_ERROR, ZB_CODE_OPEN_TO_TRAFFIC, ZB_CODE_CLOSED_TO_TRAFFIC
)
from .utils import (
    try_parse_int_or_default,
    verify_index_or_default,
    remove_html_tags,
    extract_match_or_default
)


ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key=DOMAIN,
        name=NAME,
        icon=ZB_ICONS[0],
    ),
)


async def async_setup_entry(hass, entry, async_add_devices):
    """Set up the sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        ZelzateBrugSensor(
            coordinator=coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class ZelzateBrugSensor(ZelzateBrugEntity, SensorEntity):
    """zelzate_brug Sensor class."""

    def __init__(
        self,
        coordinator: ZelzateBrugDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str:
        """Return the status of the sensor."""
        statusCode = self.coordinator.data.get("statusCode")
        statusText = self.coordinator.data.get("statusText")
        index = try_parse_int_or_default(statusCode, ZB_CODE_ERROR)
        if index == ZB_CODE_ERROR:
            return "Unknown"
        elif index == ZB_CODE_OPEN_TO_TRAFFIC:
            return "Open to traffic"
        elif index == ZB_CODE_CLOSED_TO_TRAFFIC:
            suffix = extract_match_or_default(
                statusText,
                ZB_TIME_PATTERN,
                "",
                " until "
            )
            return "Closed to traffic" + suffix
        else:
            return "Closing to traffic soon"

    @property
    def icon(self):
        index = try_parse_int_or_default(
            self.coordinator.data.get("statusCode"),
            ZB_DEFAULT_ICON
        )
        return ZB_ICONS[verify_index_or_default(
            index,
            len(ZB_ICONS),
            ZB_DEFAULT_ICON
        )]

    @property
    def extra_state_attributes(self):
        """Return attributes for sensor."""
        if not self.coordinator.data:
            return {}
        attributes = {
            "last_synced": datetime.now(),
            "status_code": self.coordinator.data.get("statusCode"),
            "status_text": remove_html_tags(self.coordinator.data.get("statusText")),
        }
        return attributes