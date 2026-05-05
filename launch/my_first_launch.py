
#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='kolocharov_pkg',           # ← замени на своё имя пакета
            executable='even_publisher',
            name='even_publisher',
            output='screen',
        ),
        Node(
            package='kolocharov_pkg',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
        ),
    ])
