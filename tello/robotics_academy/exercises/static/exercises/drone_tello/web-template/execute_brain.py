from hal import HAL
import time

drone = HAL()

drone.takeoff()
print("Drone despegado!")

time.sleep(5)

drone.land()
print("aterrizo...")

while True:
    pass