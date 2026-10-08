import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8

import random

class BatteryPublisher(Node):
    
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(Int8, 'battery_health_topic', 10 )
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.battery_callback)
        self.battery_start = 100
        
    def battery_callback(self):
        msg = Int8()
        msg.data = self.battery_start
        if random.randint(0,1) > 0:
            self.battery_start -= 1
        self.publisher_.publish(msg)
        self.get_logger().info('Battery health is "%i"' % msg.data)
        
def main():
    rclpy.init()
    battery_publisher = BatteryPublisher()
    rclpy.spin(battery_publisher)
    
    battery_publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()