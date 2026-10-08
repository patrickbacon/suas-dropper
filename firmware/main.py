from machine import Pin, I2C, PWM
import time

ON_LUX = 200
OFF_LUX = 120
REST_ANGLE = 0
ACTIVE_ANGLE = 90
SERVO_PIN = 15
POLL_MS = 100

BH1750_ADDR = 0x23
BH1750_CONT_HIRES = 0x10

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100_000)
i2c.writeto(BH1750_ADDR, bytes([BH1750_CONT_HIRES]))
time.sleep_ms(180)


def read_lux():
    raw = i2c.readfrom(BH1750_ADDR, 2)
    return ((raw[0] << 8) | raw[1]) / 1.2


servo = PWM(Pin(SERVO_PIN))
servo.freq(50)


def set_angle(deg):
    us = 1000 + (deg / 180) * 1000
    duty = int(us / 20000 * 65535)
    servo.duty_u16(duty)


set_angle(REST_ANGLE)
triggered = False

while True:
    lux = read_lux()

    if not triggered and lux > ON_LUX:
        triggered = True
        set_angle(ACTIVE_ANGLE)
        print("LED ON  ({:.0f} lux) -> servo to {}".format(lux, ACTIVE_ANGLE))

    elif triggered and lux < OFF_LUX:
        triggered = False
        set_angle(REST_ANGLE)
        print("LED OFF ({:.0f} lux) -> servo to {}".format(lux, REST_ANGLE))

    time.sleep_ms(POLL_MS)
