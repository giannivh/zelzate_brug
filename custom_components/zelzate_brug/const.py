"""Constants for zelzate_brug."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Zelzate Brug"
DOMAIN = "zelzate_brug"
VERSION = "1.0.0"
ATTRIBUTION = "Data provided by https://www.zelzatebrug.vlaanderen/"

ZB_ICONS = ["mdi:boom-gate-up", "mdi:boom-gate", "mdi:boom-gate-alert"]
ZB_DEFAULT_ICON = 2
ZB_TIME_PATTERN = r'\b\d{1,2}:\d{2}\b'
ZB_HTML_TAGS = r'<[^>]*>'
ZB_CODE_ERROR = -1
ZB_CODE_OPEN_TO_TRAFFIC = 0
ZB_CODE_CLOSED_TO_TRAFFIC = 1
