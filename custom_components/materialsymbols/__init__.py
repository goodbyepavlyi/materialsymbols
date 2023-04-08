import logging
import json
from os import walk, path
from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http.view import HomeAssistantView

_LOGGER = logging.getLogger(__name__)
DOMAIN = "materialsymbols"
LOADER_URL = f"/{DOMAIN}/materialsymbols.js"
LOADER_PATH = f"custom_components/{DOMAIN}/materialsymbols.js"
ICONS_URL = f"/{DOMAIN}/icons"
ICONLIST_URL = f"/{DOMAIN}/list"
ICONS_PATH = f"custom_components/{DOMAIN}/data"

class SymbolsView(HomeAssistantView):
    requires_auth = False
    
    def __init__(self, url, iconpath):
        self.url = url
        self.iconpath = iconpath
        self.name = "Icon Listing"
    
    async def get(self, request):
        icons = []
        for (dirpath, dirnames, filenames) in walk(self.iconpath):
            icons.extend([{"name": path.join(dirpath[len(self.iconpath):], fn[:-4])} for fn in filenames if fn.endswith(".svg")])
        return json.dumps(icons)

async def async_setup(hass, config):
    hass.http.register_static_path(LOADER_URL, hass.config.path(LOADER_PATH), True)
    add_extra_js_url(hass, LOADER_URL)
    for iset in ["outlined", "rounded", "sharp"]:
        hass.http.register_static_path(ICONS_URL + "/" + iset, hass.config.path(ICONS_PATH + "/" + iset), True)
        hass.http.register_view(SymbolsView(ICONLIST_URL + "/" + iset, hass.config.path(ICONS_PATH + "/" + iset)))
    return True

async def async_setup_entry(hass, entry):
    return True

async def async_remove_entry(hass, entry):
    return True
