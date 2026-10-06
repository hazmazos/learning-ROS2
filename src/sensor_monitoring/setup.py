from setuptools import find_packages, setup

package_name = 'sensor_monitoring'

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
    maintainer_email='hamza@todo.todo',
    description='Mock publisher for IMU and distance sensor with listener',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'imu_talker = sensor_monitoring.imu_data_pub:main',
            'distance_talker = sensor_monitoring.distance_data_pub:main',
            'sensor_listener = sensor_monitoring.sensor_monitor_sub:main',
        ],
    },
)
