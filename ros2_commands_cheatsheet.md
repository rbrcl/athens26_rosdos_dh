# ROSDOS workflow cheatsheet <!-- omit in toc -->

## TOC <!-- omit in toc -->
- [Terminal basics](#terminal-basics)
- [Sourcing Environment](#sourcing-environment)
- [Built-in basics](#built-in-basics)
- [Create ros2 service](#create-ros2-service)
- [Examples](#examples)
    - [](#)
    - [](#-1)
    - [](#-2)


## Terminal basics

```bash
$ cd ~/                 # Go to the home directory
$ mkdir ros2_athens_ws  # Create the workspace folder
$ cd ros2_athens_ws     # Access the workspace folder
$ mkdir src             # Create the source folder
$ colcon build          # Build your environment
```

1. Use ros2 commands to create a package: 
```bash
# Go to the ws source directory
$ cd ~/ros2_athens_ws/src
# Create the new package
$ ros2 pkg create --build-type ament_python first_package --dependencies rclpy std_msgs
```
```bash
# Create interfaces package
$ ros2 pkg create first_interfaces --build-type ament_cmake --dependencies std_msgs
```
2. Build the new package:
```bash
$ cd ~/ros2_athens_ws # Go to the ws directory
$ colcon build # Build the new package
```

3. Use ros2 commands to look for your built package
```bash
$ ros2 pkg list | grep “first_package ”

```

4. Do you see the package?
```bash
$ source ~/ros2_athens_ws/install/local_setup.bash
```

## Running a node

1. build it, source it

```bash
$ cd ~/ros2_athens_ws         # Go to the ws directory
$ colcon build                # Build your environment
$ source install/setup.bash   # Source it
```
2. run the node

```bash

```


## Sourcing Environment

Manual Sourcing:
Every time you open a new terminal, you will need to manually source your workspace:

```bash
$ source ~/ros2_athens_ws/install/local_setup.bash
```

Automate Sourcing:
Every time you open a terminal it is executed this file `~/.bashrc`.
We can add to it the source line so we don’t need to sourcece it manually every time:

1. Edit the ~/.bashrc using “nano”:
```bash
$ nano ~/.bashrc
```
2. Add the following line at the end of the file:
3. Save and close it with `ctr + x`
4. Open a new terminal and check if your can see the node:
```bash
$ ros2 pkg list | grep “first_package ”
```

## Built-in basics

```bash
$ rqt_graph			            # Visualization
$ ros2 node list 		        # Lists all active nodes
$ ros2 topic list 		      # Lists all active topics
$ ros2 topic echo <topic_name>	# Prints messages
$ ros2 topic info <topic_name> 	# Information of topic
$ ros2 topic hz <topic_name> 	  # Publish rate
```

```bash
$ ros2 interface list
$ ros2 interface show <desired_interfaces>
```

```bash
$ ros2 service list
$ ros2 service call /service_name <srv_type> "{field1: value1}"
```

## Create ros2 service

1. Define the Service File:
In the `stm_interfaces` create a new folder called `/srv`
Create a new file inside called AddTwoInts.srv:
```
int32 a
int32 b
---
int32 sum
```

2. Add the Service to the `CMakeLists.txt`
Add the service to `rosidl_generate_interfaces` (as we did with the
custom msgs)
```
rosidl_generate_interfaces(${PROJECT_NAME}
  // Other custom interfaces
  "srv/AddTwoInts.srv")
```

3. Compile and check your new service using ros2 comands
```bash
$ ros2 interfaces list | grep “AddTwoInts”
$ ros2 interfaces AddTwoInts show
```

## Examples

```bash
$ ros2 run demo_nodes_cpp talker
$ ros2 run demo_nodes_cpp listener
```

```bash
$ ros2 run turtlesim turtlesim_node
$ ros2 run turtlesim turtle_teleop_key
```

####

```bash

```
####

```bash

```
####

```bash

```


```bash

```


```bash

```


```bash

```