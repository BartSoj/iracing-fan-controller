from miio import DeviceFactory

fan = DeviceFactory.create("192.168.1.225", "647137208daf99bbc7d9103a085a6c8a")

print("turning on...")
fan.on()

print("speed: " + str(fan.status().speed))
while True:
    speed = int(input("speed: "))
    if speed < 0 or speed > 100:
        print("invalid speed")
        continue
    fan.set_speed(speed)
