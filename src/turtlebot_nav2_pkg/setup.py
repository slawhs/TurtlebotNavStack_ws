

import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'turtlebot_nav2_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('map/*')),
        (os.path.join('share', package_name), glob('nav2_params.yaml')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='slawhs',
    maintainer_email='ignagaja@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
