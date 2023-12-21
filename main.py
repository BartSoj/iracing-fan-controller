from miio import DeviceFactory
import irsdk
import time

# Initialize the fan
fan = DeviceFactory.create("192.168.1.225", "647137208daf99bbc7d9103a085a6c8a")
fan.on()
print("Fan turned on...")

# Initialize iRacing SDK
ir = irsdk.IRSDK()
def wait_for_iracing():
    while not ir.startup():
        print('Waiting for iRacing...')
        time.sleep(1)

wait_for_iracing()

try:
    while True:
        # Check if iRacing is still connected
        if ir.is_initialized and ir.is_connected:
            # Fetch the car speed (m/s), convert it to a suitable scale for fan speed
            car_speed = ir['Speed']  # Speed in meters per second
            fan_speed = int(car_speed * scaling_factor)  # Scale it appropriately

            # Ensure the fan speed is within valid range
            fan_speed = max(0, min(fan_speed, 100))

            # Set the fan speed
            fan.set_speed(fan_speed)
            print(f"Car speed: {car_speed} m/s, Fan speed: {fan_speed}")
        else:
            wait_for_iracing()

        time.sleep(1)  # Update interval

except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    fan.off()
    print("Fan turned off.")