import rclpy
from rclpy.node import Node
from battery_monitoring_interface.srv import BatteryHealth

class BatteryClient(Node):
    def __init__(self):
        super().__init__('battery_health_client')
        self.cli = self.create_client(BatteryHealth, 'battery_health_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available yet ...')
        self.req = BatteryHealth.Request()

    def send_request(self):
        return self.cli.call_async(self.req)

def main():
    rclpy.init()
    battery_client = BatteryClient()
    future = battery_client.send_request()
    rclpy.spin_until_future_complete(battery_client, future)
    response = future.result()
    battery_client.get_logger().info('Battery health is "%i"' % response.battery_health)

    battery_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()