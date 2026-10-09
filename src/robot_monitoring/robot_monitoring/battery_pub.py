import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
from battery_monitoring_interface.srv import BatteryHealth

import random

class BatteryPublisher(Node):
    
    def __init__(self):
        super().__init__('battery_publisher')
        self.publisher_ = self.create_publisher(Int8, 'battery_health_topic', 10 )
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.battery_callback)
        self.battery_health = 100

        self.battery_srv = self.create_service(BatteryHealth, 'battery_health_service', self.battery_srv_callback)

        
    def battery_callback(self):
        msg = Int8()
        msg.data = self.battery_health
        if random.randint(0,1) > 0:
            self.battery_health -= 1
        self.publisher_.publish(msg)
        self.get_logger().info('Battery health is "%i"' % msg.data)

    def battery_srv_callback(self ,_request, response): 
        response.battery_health = self.battery_health
        return response
        
def main():
    rclpy.init()
    battery_publisher = BatteryPublisher()
    rclpy.spin(battery_publisher)
    
    battery_publisher.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()