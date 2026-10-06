import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32

class SensorSubscriber(Node):

    def __init__(self):
        super().__init__('sensor_sub')
        self.imu_subscription_ = self.create_subscription(Vector3, 'imu_topic', self.imu_callback, 10)
        self.distance_subscription_ = self.create_subscription(Float32, 'distance_topic', self.distance_callback, 10)
        self.imu_subscription_
        self.distance_subscription_

    def imu_callback(self, msg):
        self.get_logger().info("IMU data: {x %.2f}, {y %.2f}, {z %.2f}\n" % (msg.x, msg.y, msg.z))

    def distance_callback(self, msg):
        self.get_logger().info("Distance data: %.2f" % msg.data)

def main():
    rclpy.init()
    sensor_subscriber = SensorSubscriber()
    rclpy.spin(sensor_subscriber)

    sensor_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()