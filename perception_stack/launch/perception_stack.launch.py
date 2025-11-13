from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='perception_stack',
            executable='lidar_node.py',
            name='lidar_node'
        ),
        Node(
            package='perception_stack',
            executable='camera_node.py',
            name='camera_node'
        ),
        Node(
            package='perception_stack',
            executable='segnet_inference.py',
            name='segnet_inference'
        ),
        Node(
            package='perception_stack',
            executable='rf_detr_inference.py',
            name='rf_detr_inference'
        )
    ])
