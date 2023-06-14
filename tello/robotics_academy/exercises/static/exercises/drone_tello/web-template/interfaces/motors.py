import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from tello_msgs.srv import TelloAction
import threading
from math import pi as PI
from .threadPublisher import ThreadPublisher



def cmdvel2Twist(vel):

    tw = Twist()
    tw.linear.x = float(vel.vx)
    tw.linear.y = float(vel.vy)
    tw.linear.z = float(vel.vz)
    tw.angular.x = float(vel.ax)
    tw.angular.y = float(vel.ay)
    tw.angular.z = float(vel.az)

    return tw


class CMDVel ():

    def __init__(self):

        self.vx = 0 # vel in x[m/s] (use this for V in wheeled robots)
        self.vy = 0 # vel in y[m/s]
        self.vz = 0 # vel in z[m/s]
        self.ax = 0 # angular vel in X axis [rad/s]
        self.ay = 0 # angular vel in X axis [rad/s]
        self.az = 0 # angular vel in Z axis [rad/s] (use this for W in wheeled robots)
        self.timeStamp = 0 # Time stamp [s]


    def __str__(self):
        s = "CMDVel: {\n   vx: " + str(self.vx) + "\n   vy: " + str(self.vy)
        s = s + "\n   vz: " + str(self.vz) + "\n   ax: " + str(self.ax) 
        s = s + "\n   ay: " + str(self.ay) + "\n   az: " + str(self.az)
        s = s + "\n   timeStamp: " + str(self.timeStamp)  + "\n}"
        return s 

class PublisherMotors(Node):
 
    def __init__(self, topic, maxV, maxW):
        super().__init__("FollowLineF1")
        self.maxW = maxW
        self.maxV = maxV

        self.topic = topic
        self.data = CMDVel()
        self.pub = self.create_publisher(Twist, topic, 10)
        
        self.cli = self.create_client(TelloAction, 'tello_action')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = TelloAction.Request()
        
        self.lock = threading.Lock()

        self.kill_event = threading.Event()
        self.thread = ThreadPublisher(self, self.kill_event)

        self.thread.daemon = True
        self.start()
 
    def publish (self):

        self.lock.acquire()
        tw = cmdvel2Twist(self.data)
        self.lock.release()
        self.pub.publish(tw)
        
    def stop(self):
   
        self.kill_event.set()
        self.pub.unregister()

    def start (self):

        self.kill_event.clear()
        self.thread.start()
        
    def getMaxW(self):
        return self.maxW

    def getMaxV(self):
        return self.maxV
        

    def sendVelocities(self, vel):

        self.lock.acquire()
        self.data = vel
        self.lock.release()

    def sendV(self, v):

        self.sendVX(v)

    def sendL(self, l):

        self.sendVY(l)

    def sendW(self, w):

        self.sendAZ(w)

    def sendVX(self, vx):

        self.lock.acquire()
        self.data.vx = vx
        self.lock.release()

    def sendVY(self, vy):

        self.lock.acquire()
        self.data.vy = vy
        self.lock.release()

    def sendAZ(self, az):

        self.lock.acquire()
        self.data.az = az
        self.lock.release()
        
    def send_request(self, cmd):
        self.req.cmd = cmd
        self.future = self.cli.call_async(self.req)
        
    def takeoff(self):
        self.send_request('takeoff')
        
    def pause(self):
        self.send_request('stop')
        
    def land(self):
        self.send_request('land')
        
    def forward(self, d):
        msg = "forward " + str(d)
        self.send_request(msg)
        
    def left(self, d):
        msg = "ccw " + str(d)
        self.send_request(msg)
        
    def right(self, d):
        msg = "cw " + str(d)
        self.send_request(msg)

