import irsdk
import time

# Initialize iRacing SDK
ir = irsdk.IRSDK()


def wait_for_iracing():
    while not ir.startup():
        print('Waiting for iRacing...')
        time.sleep(1)


wait_for_iracing()

while True:
    # Check if iRacing is still connected
    if ir.is_initialized and ir.is_connected:
        # Fetch the car speed (m/s), convert it to a suitable scale for fan speed
        car_speed = ir['Speed']  # Speed in meters per second
        print(f"Car speed: {car_speed} m/s")
    else:
        wait_for_iracing()

    time.sleep(1)  # Update interval
