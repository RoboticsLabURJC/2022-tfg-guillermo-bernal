from shared.image import SharedImage
from shared.value import SharedValue
import numpy as np
import cv2

# Define HAL functions
class HALFunctions:
    def __init__(self):
        # Initialize image variable
        self.shared_image = SharedImage("halimage")
        self.take_off = SharedValue("takkeoff")
        self.landing = SharedValue("land")

    # Get image function
    def getImage(self):
        image = self.shared_image.get()
        return image

    # Send velocity function
    def takeoff(self, velocity):
        self.take_off.add(velocity)

    # Send angular velocity function
    def land(self, angular):
        self.landing.add(angular)

# Define GUI functions
class GUIFunctions:
    def __init__(self):
        # Initialize image variable
        self.shared_image = SharedImage("guiimage")

    # Show image function
    def showImage(self, image):
        # Reshape to 3 channel if it has only 1 in order to display it
        if (len(image.shape) < 3):
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        self.shared_image.add(image)