from miio import DeviceFactory
import irsdk
import time

fan = DeviceFactory.create("192.168.1.225", "647137208daf99bbc7d9103a085a6c8a")
fan.on()
print("Fan turned on...")

ir = irsdk.IRSDK()


def wait_for_iracing():
    while not ir.startup():
        print('Waiting for iRacing...')
        time.sleep(1)


wait_for_iracing()

fan_speed = 0

try:
    while True:
        if ir.is_initialized and ir.is_connected:
            car_speed = ir['Speed']
            brake = ir['Brake']
            throttle = ir['Throttle']
            gear = ir['Gear']
            acceleration = ir['VertAccel']

            new_fan_speed = car_speed // 2.5

            new_fan_speed = max(0, min(fan_speed, 100))

            if fan_speed != new_fan_speed:
                fan.set_speed(new_fan_speed)
                fan_speed = new_fan_speed

            print(f"Car speed: {car_speed} m/s, Fan speed: {fan_speed}")
        else:
            wait_for_iracing()

        time.sleep(.5)

except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    fan.off()
    print("Fan turned off.")
