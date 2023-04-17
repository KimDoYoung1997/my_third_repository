import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory       
from launch.actions import DeclareLaunchArgument
from launch.actions import LogInfo
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir

def generate_launch_description():
    return LaunchDescription([

        LogInfo(msg=['Execute three launch files!']),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                    [ThisLaunchFileDir(), '/test.launch.py']),
            ),      

    ])
    