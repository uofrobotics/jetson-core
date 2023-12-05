#!/usr/bin/python3
import time
import serial

# https://jetsonhacks.com/2019/10/10/jetson-nano-uart/
# https://github.com/JetsonHacksNano/UARTDemo/blob/master/uart_example.py
SERIAL_READ_TIMEOUT = 1

serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=SERIAL_READ_TIMEOUT # wait at most one second for a response from nucleo
)
# Wait a second to let the port initialize
time.sleep(1)

control_rev = 129
control_forward = 144
speed_fast = 70
speed_slow = 30

def control_motors(fl: int, fr: int, bl: int, br: int):
    assert fl <= 127
    assert fr <= 127
    assert bl <= 127
    assert br <= 127

try:

    # TODO: add a new control block that the jetson says to unlock/recover from locked motors
    while True:
        serial_port.write(control_forward.to_bytes(1, 'big'))
        # any slower and motor speed commands are not reliable
        time.sleep(0.001)

        serial_port.write(speed_fast.to_bytes(1, 'big'))
        time.sleep(0.001)

        serial_port.write(speed_fast.to_bytes(1, 'big'))
        time.sleep(0.001)

        serial_port.write(speed_fast.to_bytes(1, 'big'))
        time.sleep(0.001)

        serial_port.write(speed_fast.to_bytes(1, 'big'))
        time.sleep(0.001)

        print(speed_fast)
        time.sleep(2)

        serial_port.write(control_forward.to_bytes(1, 'big'))
        time.sleep(0.001)

        serial_port.write(speed_slow.to_bytes(1, 'big'))
        time.sleep(0.001)

        serial_port.write(speed_slow.to_bytes(1, 'big'))
        time.sleep(0.001)

        serial_port.write(speed_slow.to_bytes(1, 'big'))
        time.sleep(0.001)

        serial_port.write(speed_slow.to_bytes(1, 'big'))
        time.sleep(0.001)

        print(speed_slow)
        time.sleep(2)


except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass