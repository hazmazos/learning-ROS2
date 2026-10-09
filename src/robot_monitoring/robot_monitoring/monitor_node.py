import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
from geometry_msgs.msg import Point
from battery_monitoring_interface.srv import BatteryHealth

class MonitorNode(Node):
    
    def __init__(self):
        super().__init__('monitor_node')
        self.battery_health = None
        self.battery_sub = self.create_subscription(Int8, 'battery_health_topic', self.battery_sub_callback, 10)
        self.battery_srv = self.create_service(BatteryHealth, 'battery_health_service', self.battery_srv_callback)
        
    
    def battery_sub_callback(self, msg):
        self.battery_health = msg.data

    def battery_srv_callback(self ,_request, response): ## to make a custom interface
        if self.battery_health is None:
            response.battery_health = -1
        else:
            response.battery_health = self.battery_health
        return response

def main():
    rclpy.init()
    monitor_node = MonitorNode()
    rclpy.spin(monitor_node)

    monitor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()