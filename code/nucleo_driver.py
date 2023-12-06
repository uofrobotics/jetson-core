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

speed_fast = 70
speed_slow = 30

# inputs are in the range [-127, 127] where positive numbers drive a motor forward, negative backwards
def control_motors(fl: int, fr: int, bl: int, br: int):
    assert fl <= 127 and fl >= -127
    assert fr <= 127 and fr >= -127
    assert bl <= 127 and bl >= -127
    assert br <= 127 and br >= -127



    # drive motor control packet between [129, 144]

    if bl > 0:
        bl_bit = 1
    else:
        bl_bit = 0

    if br > 0:
        br_bit = 1
    else:
        br_bit = 0

    if fl > 0:
        fl_bit = 1
    else:
        fl_bit = 0

    if fr > 0:
        fr_bit = 1
    else:
        fr_bit = 0

    

    motor_dir_control_packet = 129 + ((bl_bit << 3) | (br_bit << 2) | (fl_bit << 1) | (fr_bit << 0))

    print(motor_dir_control_packet)
    serial_port.write(motor_dir_control_packet.to_bytes(1, 'big'))
    # any slower and motor speed commands are not reliable
    time.sleep(0.001)

    serial_port.write(abs(bl).to_bytes(1, 'big'))
    time.sleep(0.001)

    serial_port.write(abs(br).to_bytes(1, 'big'))
    time.sleep(0.001)

    serial_port.write(abs(fl).to_bytes(1, 'big'))
    time.sleep(0.001)

    serial_port.write(abs(fr).to_bytes(1, 'big'))
    time.sleep(0.001)

try:

    # TODO: add a new control block that the jetson says to unlock/recover from locked motors

    
    while True:
        #control_motors(20, 20, 20, 20)

        time.sleep(1)
        control_motors(fl=-20, fr=-20, bl=20, br=20)


        time.sleep(1)


except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass