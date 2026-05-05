import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):

    def __init__(self):
        super().__init__('overflow_listener')

        # параметры
        self.declare_parameter('even_topic', '/even_numbers')
        self.declare_parameter('overflow_topic', '/overflow')

        even_topic = self.get_parameter('even_topic').value
        overflow_topic = self.get_parameter('overflow_topic').value

        # подписка на even
        self.sub_even = self.create_subscription(
            Int32,
            even_topic,
            self.even_callback,
            10
        )

        # подписка на overflow
        self.sub_overflow = self.create_subscription(
            Int32,
            overflow_topic,
            self.overflow_callback,
            10
        )

        self.get_logger().info(
            f'Listening even: {even_topic}, overflow: {overflow_topic}'
        )

    def even_callback(self, msg: Int32):
        self.get_logger().info(f'Even: {msg.data}')

    def overflow_callback(self, msg: Int32):
        self.get_logger().warn(
            f'!!! ПЕРЕПОЛНЕНИЕ !!! value: {msg.data}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
