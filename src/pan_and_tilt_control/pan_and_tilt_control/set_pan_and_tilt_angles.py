import rclpy
from rclpy.node import Node
from pan_and_tilt_interface.srv import Angles
import sys

class PanAndTiltClient(Node):
    def __init__(self):
        super().__init__('pan_and_tilt_client')
        self.cli = self.create_client(Angles, 'pan_and_tilt_angles')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available yet ...')
        self.req = Angles.Request()

    def send_request(self, pan_angle, tilt_angle):
        self.req.pan_angle = pan_angle
        self.req.tilt_angle = tilt_angle
        return self.cli.call_async(self.req)

def main():
    rclpy.init()
    pan_and_tilt_client = PanAndTiltClient()
    future = pan_and_tilt_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(pan_and_tilt_client, future)
    response = future.result()
    pan_and_tilt_client.get_logger().info(
        'Tried to send angles -> %s' 
        % (response.status)
    )

    pan_and_tilt_client.destroy_node()
    rclpy.shutdown()