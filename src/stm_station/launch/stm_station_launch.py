from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
 
 
def generate_launch_description():
    share_dir = get_package_share_directory('arduino_station')
 
    serial_params = os.path.join(
        share_dir,
        'config',
    )
 
    return LaunchDescription([
        
        # 1. Launch the Serial Node (The hardware bridge)
        Node(
            package='arduino_station',
            executable='arduino_pub_sub_node',
            name='serial_node',
            parameters=[serial_params],
            output='screen'
        ),

        # 2. Launch the Control Node (The brain)
        Node(
            package='arduino_station',
            executable='arduino_control_node',
            name='control_node',
            parameters=[
                {'master_group_id': 1},
                {'slave_group_id': 2}
            ],
            output='screen'
        )
    ])