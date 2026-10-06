import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TemperatureSubscriber(Node):
    def __init__(self):
        super().__init__('temp_sub')
        self.subscription_ = self.create_subscription(Float32, 'temp_topic', self.listener_callback, 10)
        self.subscription_

    def listener_callback(self, msg):
        self.get_logger().info('I heard "%.2f"' % msg.data)

        if msg.data > 28.0:
            self.get_logger().warn("Temperature too high")

def main():
    rclpy.init()
    temp_subscriber = TemperatureSubscriber()
    rclpy.spin(temp_subscriber)

    temp_subscriber.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()