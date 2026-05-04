import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):

    def __init__(self):
        super().__init__('even_pub')

        self.pub_even = self.create_publisher(Int32, '/even_numbers', 10)
        self.pub_overflow = self.create_publisher(Int32, '/overflow', 10)

        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Гц
        self.current = 0

    def timer_callback(self):
        # 1. ВСЕГДА публикуем текущее число
        msg = Int32()
        msg.data = self.current
        self.pub_even.publish(msg)

        self.get_logger().info(f'Even: {self.current}')

        # 2. Проверяем переполнение
        if self.current >= 100:
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

if __name__ == '__main__':
    main()
