from setuptools import find_packages, setup

package_name = 'pan_and_tilt_control'

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
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'pan_and_tilt_service = pan_and_tilt_control.pan_and_tilt_controller:main',
            'pan_and_tilt_client = pan_and_tilt_control.set_pan_and_tilt_angles:main',
        ],
    },
)
