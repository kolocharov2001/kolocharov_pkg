import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/i-mv/ros2_ws/src/kolocharov_pkg/install/kolocharov_pkg'
