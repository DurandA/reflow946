# Reflow946

The Reflow946 is a Bluetooth LE temperature controller for the 946C electronic hot plate. Using this controller, a reflow profile can be programmed from your web browser using the [Web Bluetooth](https://webbluetoothcg.github.io/web-bluetooth/) API. You can use preset profiles (e.g. for lead-free or leaded soldering) or create a custom profile for a perfect cheese fondue. 🫕

![UYUE-946C](https://github.com/DurandA/reflow946/wiki/images/UYUE-946C.png)

The controller board is intended to replace the original controller board. It is **only compatible with the 3 buttons variant** pictured above (see this [teardown](https://youtu.be/Gv2sRJ9y_Ok)). Please send a PR if you adapted the design to a new variant.

## Hardware

The controller is based on a ESP32 module with an IPEX antenna. Since the metal case acts as a Faraday cage, the BLE signal can be improved by taping an antenna outside of the case.

### Front

![PCB front](https://github.com/DurandA/reflow946/wiki/images/front.png)

### Back

![PCB back](https://github.com/DurandA/reflow946/wiki/images/back.png)

## Status

- [x] Temperature control
  - [x] Temperature control using the front panel
  - [ ] BLE GATT service for temperature control
- [ ] Reflow profile programming
  - [ ] BLE GATT service for reflow profiles
  - [ ] Web Bluetooth application
