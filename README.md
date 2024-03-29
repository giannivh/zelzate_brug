<img src="https://github.com/giannivh/zelzate_brug/raw/main/img/brand/brand.jpg"
     alt="Zelzate Brug"
     align="right"
     style="width: 75px;margin-right: 10px;" />

# Zelzate Brug for Home Assistant

A Home Assistant integration to monitor the Zelzate Brug services.

Data provided by https://www.zelzatebrug.vlaanderen/

[![github release](https://img.shields.io/github/release/giannivh/zelzate_brug.svg?style=for-the-badge&logo=github)](https://github.com/giannivh/zelzate_brug/releases)
[![github commit activity](https://img.shields.io/github/commit-activity/y/giannivh/zelzate_brug.svg?style=for-the-badge&logo=github)](https://github.com/giannivh/zelzate_brug/commits/main)
[![MIT License](https://img.shields.io/github/license/giannivh/zelzate_brug.svg?style=for-the-badge)](https://github.com/giannivh/zelzate_brug/blob/main/LICENSE)

[![maintainer](https://img.shields.io/badge/maintainer-Gianni%20Van%20Hoecke%20%40giannivh-blue.svg?style=for-the-badge&logo=github)](https://github.com/giannivh)

## Installation

### Using [HACS](https://hacs.xyz/) (recommended)

**Click on this button:**

[![Open your Home Assistant instance and open the repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg?style=flat-square)](https://my.home-assistant.io/redirect/hacs_repository/?owner=giannivh&repository=zelzate_brug&category=integration)

**Or follow these steps:**

1. Simply search for `Zelzate Brug` in HACS and install it easily.
2. Restart Home Assistant.
3. Add the 'Zelzate Brug' integration via HA Settings > 'Devices and Services' > 'Integrations'

### Manual

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `zelzate_brug`.
4. Download _all_ the files from the `custom_components/zelzate_brug/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant.
7. Add the 'Zelzate Brug' integration via HA Settings > 'Devices and Services' > 'Integrations'

**This integration will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from Zelzate Brug API.

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Screenshots

![screenshot-01](https://raw.githubusercontent.com/giannivh/zelzate_brug/main/img/screenshots/zb_01.png)

![screenshot-02](https://raw.githubusercontent.com/giannivh/zelzate_brug/main/img/screenshots/zb_02.png)

![screenshot-03](https://raw.githubusercontent.com/giannivh/zelzate_brug/main/img/screenshots/zb_03.png)

![screenshot-04](https://raw.githubusercontent.com/giannivh/zelzate_brug/main/img/screenshots/zb_04.png)

## Code origin

The code of this Home Assistant integration has been written by analysing the calls made by the Zelzate Brug website. I have no link with Zelzate Brug.