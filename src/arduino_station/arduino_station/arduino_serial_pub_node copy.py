import rclpy
from rclpy.node import Node
import serial
from arduino_interfaces.msg import Mpu6050Data # Your custom message

class ArduinoSerialPublisher(Node):
    def __init__(self):
        super().__init__('arduino_serial_pub_node')
        self.publisher_ = self.create_publisher(Mpu6050Data, 'mpu6050_data', 10)
        
        # Adjust '/dev/ttyACM0' to your Arduino port
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        # self.get_logger().info("Connected to Arduino on /dev/ttyACM0")
        
        self.timer = self.create_timer(0.01, self.timer_callback)

    def timer_callback(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').strip()
            data = line.split(',')
            
            if len(data) == 10:
                try:
                    msg = Mpu6050Data()
                    msg.w, msg.x, msg.y, msg.z = map(float, data[0:4])
                    msg.accel_x, msg.accel_y, msg.accel_z = map(float, data[4:7])
                    msg.gyro_x, msg.gyro_y, msg.gyro_z = map(float, data[7:10])
                    
                    self.publisher_.publish(msg)
                except ValueError:
                    self.get_logger().warn(f"Malformed data received: {line}")

def main(args=None):
    rclpy.init(args=args)
    node = ArduinoSerialPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()