import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ScaredRobot(Node):

    def listener_callback(self, msg):
        print(msg.data)
        right = int(msg.data[:-2]) #remove the 'cm' and convert to int.
        msg = String()
        
        if right < 10:
            
            msg.data = "TURNL:0050\n"
            self.publisher.publish(msg)
        
        msg.data = "CONTF:0100\n"
        self.publisher.publish(msg)


    def __init__(self):
        super().__init__('ScaredRobot')
        self.publisher = self.create_publisher(String, '/robot/control', 10)
        msg = String()
        msg.data = "CONTF:0100\n"
        self.publisher.publish(msg)

        self.subscription = self.create_subscription(
            String,
            '/robot/right',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

def main(args=None):
    rclpy.init(args=args)

    scaredrobot = ScaredRobot()
    rclpy.spin(scaredrobot)
    
    scaredrobot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
