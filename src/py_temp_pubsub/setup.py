from setuptools import find_packages, setup

package_name = 'py_temp_pubsub'

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
    description='Applying the pubsub example to a mock sensor reading',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'temp_talker = py_temp_pubsub.temp_pub:main',
            'temp_listener = py_temp_pubsub.temp_sub:main',
        ],
    },
)
