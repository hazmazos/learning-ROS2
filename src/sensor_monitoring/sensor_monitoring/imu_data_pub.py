import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

import random

class ImuPublisher(Node):
    
    def __init__(self):
        super().__init__('imu_pub')
        self.publisher_ = self.create_publisher(Vector3, 'imu_topic', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def timer_callback(self):
        msg = Vector3
        msg.x = random.uniform(0.0, 1.0)
        msg.y = random.uniform(0.0, 1.0)
        msg.z = random.unifrom(0.0, 1.0)
        self.publisher_.publish(msg)
        self.logger().info('Publishing "%.2f"' % msg)
        
def main():
    rclpy.init()
    imu_publisher = ImuPublisher()
    rclpy.spin(imu_publisher)
    
    imu_publisher.destroy_node()
    rclpy.shutdown()
        
    