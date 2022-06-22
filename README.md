# TP RVIZ ROS

## Installation

Make a git clone of the git repository
```sh
https://github.com/Ashamyu/TP_Noter_ROS.git
```
## Part 1
```sh
cd master
cd shamyu_ws
source devel/setup.bash
roscore
rosrun marker_visualizer publish_marker.py /vis_marker:=/marker_test
rviz
```

## Part 2
```sh

source devel/setup.bash
roscore
rosrun marker_visualizer publish_marker_array.py /vis_marker:=/space_delimiter
rviz
```

## Part 3
```sh

source devel/setup.bash
roscore
rosrun marker_visualizer randomwalk.py
rviz
```

## Part 4
```sh

source devel/setup.bash
roscore
rosrun marker_visualizer random_walk.py
rviz
```

On RVIZ click :
1 - ADD
2 - BY TOPIC  
3 - SELECT THE TOPIC



