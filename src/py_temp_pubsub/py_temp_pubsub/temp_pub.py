import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

import random 

class TemperaturePublisher(Node):

    def __init__(self):
        super().__init__('temp_pub')
        self.publisher_ = self.create_publisher(Float32, 'temp_topic', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(15.0,30.0)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%.2f"' % msg.data)

def main():
    rclpy.init()
    temp_publisher = TemperaturePublisher()
    rclpy.spin(temp_publisher)

    temp_publisher.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()
