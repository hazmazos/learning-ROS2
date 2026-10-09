from setuptools import find_packages, setup

package_name = 'robot_monitoring'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hamza',
    maintainer_email='hamzasarwari426@gmail.com',
    description='Mock sensor and battery monitoring to mimic a basic robotic system',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'battery_talker = robot_monitoring.battery_pub:main',
            'position_talker = robot_monitoring.position_pub:main',
            'monitor_node = robot_monitoring.monitor_node:main',
            'battery_client = robot_monitoring.battery_client:main'
        ],
    },
)
