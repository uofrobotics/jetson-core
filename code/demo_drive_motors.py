from nucleo_driver import MotorDriver
import time
motor_driver = MotorDriver()

try:

    while True:
        motor_driver.control_motors(fl=20, fr=20, bl=20, br=20)
        print(20)

        time.sleep(1)
        motor_driver.control_motors(fl=-20, fr=-20, bl=-20, br=-20)
        print(-20)

        time.sleep(1)


except KeyboardInterrupt:
    print("Exiting Program")

finally:
    motor_driver.close()
