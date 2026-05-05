from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'kolocharov_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
        glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='i-mv',
    maintainer_email='i-mv@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'even_publisher = kolocharov_pkg.scripts.even_number_publisher:main',
            'overflow_listener = kolocharov_pkg.scripts.overflow_listener:main',
            'listener = kolocharov_pkg.scripts.listener:main',
            'talker = kolocharov_pkg.scripts.talker:main',
            'first_node = kolocharov_pkg.scripts.first_node:main',
            'time_printer = kolocharov_pkg.scripts.time_printer:main',
        ],
    },
)
