from GUI import GUI
from HAL import HAL
import cv2

PERSON_ID = 0

def draw_center_point(img, bbox):
    """
    inputs:
    	- img: Original image where bbox will be drawn
    	- bbox: list[4] with x0,y0 and x1,y1 coordinates of a box detected by yolo algorithm
    outputs:
        - center_x: x coordinate of the center of the box
        - center_y: y coordinate of the center of the box
    """ 
    center_x = int((bbox[0] + bbox[2]) / 2)
    center_y = int((bbox[1] + bbox[3]) / 2)
    radius = 3
    color = (0, 0, 255)
    thickness = -1
    cv2.circle(img, (center_x, center_y), radius, color, thickness)

    return center_x, center_y

# YOLO initializer
yolo = HAL.YOLO()

# PD constants and error/last_error for rotation PID and height PID 
Kp_w = 0.2
Kd_w = 0.2
last_error_w = 0
error_w = 0

Kp_z = 0.15
Kd_z = 0.15
last_error_z = 0
error_z = 0

# Drone take off
HAL.takeoff()

while True:
    # Get image from drone camera
    img = HAL.getImage()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # From image, get boxes, confidence and ids of the objects detected by YOLO
    bbox, cls_conf, cls_ids = yolo(img_rgb)

    height, width, channels = img.shape

    sent = False

    # YOLO detected >=1 objects in the image
    if bbox is not None:
    	# YOLO draw the boxes with the id and conf in the image
        img = yolo.draw_boxes(img, bbox, cls_ids, cls_conf)
        for i in range(len(cls_ids)):
            if cls_ids[i] == PERSON_ID: # We only want to detect people in the image
                w = 0
                x = 0
                z = 0
                center_x, center_y = draw_center_point(img, bbox[i])
                error_w = (width / 2) - center_x
                error_z = (height / 2) - center_y
                w = Kp_w * error_w + Kd_w * (error_w - last_error_w)
                x = 20 # YOLO can get depth from image so we use a constant x
                z = Kp_z * error_z + Kd_z * (error_z - last_error_z)
                sent = True
                last_error_w = error_w
                last_error_z = error_z
        GUI.showImage(img)

    # If no person was detected in this iteration, drone will be in pause state
    if not sent:
        HAL.setRC(0,0,0,0)
    else:
        HAL.setRC(0,x,z,w)