import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
from geometry_msgs.msg import Point

class MonitorNode(Node):
    
    def __init__(self):
        super().__init__('monitor_node')

        self.battery_health = None
        self.battery_sub = self.create_subscription(Int8, 'battery_health_topic', self.battery_sub_callback, 10)

        self.x = None
        self.y = None
        self.z = None
        self.distance_sub = self.create_subscription(Point, 'position_topic', self.distance_sub_callback, 10)


        
    
    def battery_sub_callback(self, msg):
        self.battery_health = msg.data
        if self.battery_health is not None:
            self.get_logger().info('I heard battery health is {%s}' % self.battery_health)

    
    def distance_sub_callback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.z = msg.z
        if self.x is not None:
            self.get_logger().info('I heard position is {%f,%f,%f}' % (self.x, self.y, self.z))
        

    


def main():
    rclpy.init()
    monitor_node = MonitorNode()
    rclpy.spin(monitor_node)

    monitor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()