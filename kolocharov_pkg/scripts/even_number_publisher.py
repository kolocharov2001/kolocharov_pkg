import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):

    def __init__(self):
        super().__init__('even_pub')

        self.declare_parameter('frequency', 10.0)
        self.declare_parameter('overflow_limit', 100)
        self.declare_parameter('even_topic', '/even_numbers')
        self.declare_parameter('overflow_topic', '/overflow')

        freq = float(self.get_parameter('frequency').value)
        self.limit = int(self.get_parameter('overflow_limit').value)

        even_topic = self.get_parameter('even_topic').value
        overflow_topic = self.get_parameter('overflow_topic').value

        self.pub_even = self.create_publisher(Int32, even_topic, 10)
        self.pub_overflow = self.create_publisher(Int32, overflow_topic, 10)

        self.timer = self.create_timer(1.0 / freq, self.timer_callback)
        self.current = 0

    def timer_callback(self):
        # 1. ВСЕГДА публикуем even
        even_msg = Int32()
        even_msg.data = self.current
        self.pub_even.publish(even_msg)

        # 2. Проверка overflow
        if self.current >= self.limit:
            overflow_msg = Int32()
            overflow_msg.data = self.current
            self.pub_overflow.publish(overflow_msg)

            self.current = 0
        else:
            self.current += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
