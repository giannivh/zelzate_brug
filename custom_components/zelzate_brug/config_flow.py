"""Adds config flow for ZelzateBrug."""
from homeassistant import config_entries
from .const import DOMAIN


class ZelzateBrugFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for ZelzateBrug."""
    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle user step."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        return self.async_create_entry(
            title="Zelzate Brug",
            data={},
        )