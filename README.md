# sUAS Dropper



![Demo](docs/demo.gif)



A compact, battery-powered payload release system for small unmanned aircraft. An I2C light sensor detects an LED signal commanded from the pilot's transmitter, triggering a servo-driven release mechanism.

## Features
- Optical trigger using a calibrated digital lux sensor (BH1750)
- Hysteresis thresholds to prevent false triggers and servo chatter
- Servo pulse range limited to 1000–2000 µs to protect mechanical end stops
- Self-contained LiPo power with onboard charging
- Hard power switch for zero standby drain and weeks of shelf life
- Runs on power-up with no operating system

## Hardware
| Component | Purpose |
|---|---|
| Raspberry Pi Pico | Microcontroller (MicroPython) |
| BH1750 | I2C digital light sensor |
| EMAX ES08MA2 | Metal-gear release servo |
| Adafruit PowerBoost 1000C | LiPo charging and 5V boost |
| 1S LiPo battery | Power |
| SS12F44 slide switch | Power on/off |
| Custom CAD housing | Mount and release mechanism |

## Wiring
| From | To |
|---|---|
| BH1750 VCC | Pico 3V3 (pin 36) |
| BH1750 SDA | Pico GP0 (pin 1) |
| BH1750 SCL | Pico GP1 (pin 2) |
| Servo signal | Pico GP15 (pin 20) |
| Servo power | PowerBoost 5V |
| Slide switch center | PowerBoost EN |
| Slide switch outer pin | GND |
| All grounds | Common ground |

## How It Works
1. The pilot switches on an LED from the transmitter.
2. The BH1750 reads light level over I2C every 100 ms.
3. When light rises above `ON_LUX`, the servo moves to the release position.
4. When light drops below `OFF_LUX`, the servo returns to rest.

## Tuning
Watch the lux readings with the LED off and on, then set `ON_LUX` well above ambient and `OFF_LUX` below it. The gap between them prevents chatter.

## Repository Structure
- `firmware/` – MicroPython code for the Pico
- `docs/` – photos and demo media
