import rclpy
from rclpy.node import Node

from pan_and_tilt_interface.srv import Angles

class PanAndTiltService(Node):

    def __init__(self):
        super().__init__('pan_and_tilt_service')
        self.srv = self.create_service(Angles, 'pan_and_tilt_angles', self.angles_callback)

    def angles_callback(self, request, response):
        if (0 <= request.pan_angle <= 180) and (0 <= request.tilt_angle <= 180):
            response.status = "PASSED"

        else:
            response.status = "FAILED"

        return response

def main():
    rclpy.init()
    pan_and_tilt_service = PanAndTiltService()
    rclpy.spin(pan_and_tilt_service)

    pan_and_tilt_service.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



    