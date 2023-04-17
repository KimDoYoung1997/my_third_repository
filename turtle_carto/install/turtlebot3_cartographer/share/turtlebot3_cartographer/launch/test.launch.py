import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory       
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    #ros_namespace= LaunchConfiguration('ros_namespace22')

    param_dir1= LaunchConfiguration(
        'param_dir1',
        default=os.path.join(
        get_package_share_directory('turtlebot3_cartographer'),
        'launch',
        'turtlesim1.yaml')
        )
    param_dir2= LaunchConfiguration(
        'param_dir2',
        default=os.path.join(
        get_package_share_directory('turtlebot3_cartographer'),
        'launch',
        'turtlesim1.yaml')
        )
    return LaunchDescription([
        DeclareLaunchArgument(
        'ros_namespace',
        default_value=os.environ['ROS_NAMESPACE'],
        
        ),



        DeclareLaunchArgument(
        'param_dir1',
        default_value=param_dir1),
        DeclareLaunchArgument(
        'param_dir2',
        default_value=param_dir2),

        Node(
        namespace="robot1",
        package='turtlesim',
        name='turtlesim1',
        executable='turtlesim_node',
        parameters=[param_dir1],
        output='screen'),

        Node(
        package='turtlesim',
        name='turtlesim2',
        executable='turtlesim_node',
        parameters=[param_dir2],
        output='screen'),
    
])




if __name__ == '__main__':
    generate_launch_description()