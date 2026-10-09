import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from example_interfaces.srv import Trigger

import random

class PositionPublisher(Node):
    
    def __init__(self):
        super().__init__('position_publisher')
        self.publisher_ = self.create_publisher(Point, 'position_topic', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.position_callback)
        self.x = 0.0
        self.reset_distance_srv = self.create_service(Trigger, 'reset_position_srv', self.reset_position_callback)

        
    
        
    def position_callback(self):
        msg = Point()
        msg.x = self.x
        msg.y = 0.0
        msg.z = 0.0
        self.x += 1.0
        self.publisher_.publish(msg)
        self.get_logger().info('Position is "%f,%f,%f"' % (msg.x, msg.y, msg.z))

    def reset_position_callback(self, _request, response):  
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        response.success = True
        response.message = 'Position has been reset'
        return response 
        
def main():
    rclpy.init()
    position_publisher = PositionPublisher()
    rclpy.spin(position_publisher)
    
    position_publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
        
    