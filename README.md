# hass-materialsymbols

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

hass-materialsymbols is a Home Assistant custom component that allows you to use free icons from the [Material Symbols](https://fonts.google.com/icons?icon.set=Material+Symbols) set.

## Installation instructions

To install hass-materialsymbols, follow these steps:

1. Install using [HACS](https://hacs.xyz) (Or copy the contents of `custom_components/materialsymbols/` to `<your config dir>/custom_components/materialsymbols/`.)
2. Restart Home Assistant.
3. Click this: [![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=materialsymbols)
   - Alternatively: Go to your integrations configuration, click Add Integration and find "Material Symbols".

## Icon sets

The icons are divided into three sets:

- Outlined
- Rounded
- Sharp

## Usage

To use the icons, find the one you want in the [gallery](https://fonts.google.com/icons?icon.set=Material+Symbols).

The three icon sets have different prefixes: `mso:`, `msr:`, and `mss:` respectively.

For example:

- To get a solid settings icon, use `mso:settings`.
- To get an outlined settings icon, use `msr:settings`.
- To get the settings logo, use `msb:settings`.

The icons are usable anywhere in Home Assistant, not only in Lovelace.

---

## FAQ

### Can I set this up in `configuration.yaml` instead?

Yes. Just add the following to your `configuration.yaml` file:

```
materialsymbols:
```
---

## Credit
* [hass-fontawesome](https://github.com/thomasloven/hass-fontawesome)