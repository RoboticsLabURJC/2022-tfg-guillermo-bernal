import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare




def generate_launch_description():
	
	pkg_tello_node = FindPackageShare(package='tello_driver').find('tello_driver')
	
	# Tello Base launch file
	tello_launch = IncludeLaunchDescription(
	    PythonLaunchDescriptionSource(os.path.join(pkg_tello_node, 'launch', 'teleop_launch.py'))
	)
	
	
	ld = LaunchDescription()
 
	ld.add_action(tello_launch)
	
	return ld
