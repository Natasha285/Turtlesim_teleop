from setuptools import setup, find_packages

setup(
    name='turtlesim_teleop',
    version='0.0.1',
    packages=find_packages(include=['turtlesim_teleop', 'turtlesim_teleop.*']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='Simple teleoperation node for turtlesim in ROS2',
    entry_points={
        'console_scripts': [
            'teleop = turtlesim_teleop.teleop:main',
        ],
    },
)

