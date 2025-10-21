import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TeleopTurtle(Node):
    def __init__(self):
        super().__init__('teleop_turtle')
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 0.0 if self.count < 4 else 1.5
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing cmd {self.count}')
        self.count += 1
        if self.count > 7:
            self.count = 0

def main(args=None):
    rclpy.init(args=args)
    node = TeleopTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
