import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
# from segnet_model import load_model, run_inference

class SegNetInference(Node):
    def __init__(self):
        super().__init__('segnet_inference')
        self.sub = self.create_subscription(Image, 'camera_image', self.callback, 10)
        self.pub = self.create_publisher(Image, 'segnet_output', 10)

    def callback(self, img_msg):
        # img = cv_bridge.imgmsg_to_cv2(img_msg, desired_encoding="bgr8")
        # mask = run_inference(img)
        # result_msg = cv_bridge.cv2_to_imgmsg(mask)
        # self.pub.publish(result_msg)
        pass  # Fill with actual inference logic

def main(args=None):
    rclpy.init(args=args)
    node = SegNetInference()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
