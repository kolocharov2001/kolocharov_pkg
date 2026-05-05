from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction

def generate_launch_description():

    mode = LaunchConfiguration('mode')

    def launch_setup(context, *args, **kwargs):
        mode_value = context.perform_substitution(mode)

        # выбор режима
        if mode_value == 'fast':
            frequency = 20.0
            limit = 50
            even_topic = '/even_numbers_fast'
        else:
            frequency = 5.0
            limit = 150
            even_topic = '/even_numbers_slow'

        overflow_topic = '/overflow'

        return [
            Node(
                package='kolocharov_pkg',
                executable='even_publisher',
                name='even_publisher',
                parameters=[{
                    'frequency': frequency,
                    'overflow_limit': limit,
                    'even_topic': even_topic,
                    'overflow_topic': overflow_topic,
                }]
            ),

            Node(
                package='kolocharov_pkg',
                executable='overflow_listener',
                name='overflow_listener',
                parameters=[{
                    'even_topic': even_topic,
                    'overflow_topic': overflow_topic,
                }]
            )
        ]

    return LaunchDescription([
        DeclareLaunchArgument(
            'mode',
            default_value='slow',
            description='fast or slow mode'
        ),

        OpaqueFunction(function=launch_setup)
    ])
