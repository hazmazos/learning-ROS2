import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger

class ResetPositionClient(Node):
    def __init__(self):
        super().__init__('reset_position_cli')
        self.cli = self.create_client(Trigger, 'reset_position_srv')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service is not available ...')
        self.req = Trigger.Request()

    def send_request(self):
        return self.cli.call_async(self.req)

def main():
    rclpy.init()
    reset_position_client = ResetPositionClient()
    future = reset_position_client.send_request()
    rclpy.spin_until_future_complete(reset_position_client, future)
    response = future.result()
    reset_position_client.get_logger().info(response.message)

    reset_position_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
