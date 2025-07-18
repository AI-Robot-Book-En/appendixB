# Practical Example Programs for Actions

## Overview

- Uses the common [StringCommand action type](https://github.com/AI-Robot-Book-En/chapter2/blob/main/airobot_interfaces/action/StringCommand.action) shared across this book.
- Example of an action server program that can accept cancels or new goals during goal processing.
- Example of an action client program that can send cancels or new goals during goal processing.
- Developed and tested on Ubuntu 22.04 with ROS Humble.
# Practical Example Programs for Actions

## Overview

- Uses the common [StringCommand action type](https://github.com/AI-Robot-Book-En/chapter2/blob/main/airobot_interfaces/action/StringCommand.action) shared across this book.
- Example of an action server program that can accept cancels or new goals during goal processing.
- Example of an action client program that can send cancels or new goals during goal processing.
- Developed and tested on Ubuntu 22.04 with ROS Humble.

## Installation

- Assume the ROS workspace is `~/airobot_ws`.
  ```
  cd ~/airobot_ws/src
  ```

- Clone the repository containing this package:
  ```
  cd ~/airobot_ws/src
  git clone https://github.com/AI-Robot-Book-En/appendixB
  ```

- Clone the repository defining the action interface:
  ```
  git clone https://github.com/AI-Robot-Book-En/chapter2
  ```

- Build the package:
  ```
  cd ~/airobot_ws
  colcon build
  source install/setup.bash
  ```

## Execution

- Terminal 1 (Action Server):
  ```
  cd ~/airobot_ws
  source install/setup.bash
  ros2 run airobot_action new_bringme_action_server_node
  ```

- Terminal 2 (Action Client):
  ```
  cd ~/airobot_ws
  source install/setup.bash
  ros2 run airobot_action test_client
  ```

## Help

## Author

Yasuhiro Masutani

## History

- 2024-10-15: Published

## License

Copyright (c) 2025 MASUTANI Yasuhiro  
All rights reserved.  
This project is licensed under the Apache License 2.0 license found in the LICENSE file in the root directory of this project.

## References

- [rclpy Actions](https://docs.ros2.org/foxy/api/rclpy/api/actions.html)
- [Understanding actions](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)
- [Writing an action server and client (Python)](https://docs.ros.org/en/humble/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html)
  - Does not explain cancellation or accepting new goals during execution.
- [Porting ROS1 SimpleActionServer to ROS2](https://qiita.com/nasu_onigiri/items/783d7ee77556528e5a52)
- [minimal_action_server package](https://github.com/ros2/examples/tree/humble/rclpy/actions/minimal_action_server)
  - Server that handles one goal at a time: [server_single_goal](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_single_goal.py)
  - Server that queues accepted goals: [server_queue_goals](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_queue_goals.py)
  - Server that processes multiple goals concurrently: [server](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server.py)
  - Server that defers and concurrently processes multiple goals: [server_defer](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_defer.py)
  - Server without creating a node class: [server_not_composable](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_not_composable.py)
- [minimal_action_client package](https://github.com/ros2/examples/tree/humble/rclpy/actions/minimal_action_client)
  - Minimal client: [client](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client.py)
  - Client that sends a cancel after sending a goal: [client_cancel](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client_cancel.py)
  - Asynchronous client: [client_asyncio](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client_asyncio.py)
  - Client without creating a node class: [client_not_composable](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client_not_composable.py)

## Installation

- Assume the ROS workspace is `~/airobot_ws`.
  ```
  cd ~/airobot_ws/src
  ```

- Clone the repository containing this package:
  ```
  cd ~/airobot_ws/src
  git clone https://github.com/AI-Robot-Book-En/appendixB
  ```

- Clone the repository defining the action interface:
  ```
  git clone https://github.com/AI-Robot-Book-En/chapter2
  ```

- Build the package:
  ```
  cd ~/airobot_ws
  colcon build
  source install/setup.bash
  ```

## Execution

- Terminal 1 (Action Server):
  ```
  cd ~/airobot_ws
  source install/setup.bash
  ros2 run airobot_action new_bringme_action_server_node
  ```

- Terminal 2 (Action Client):
  ```
  cd ~/airobot_ws
  source install/setup.bash
  ros2 run airobot_action test_client
  ```

## Help

## Author

Yasuhiro Masutani

## History

- 2024-10-15: Published

## License

Copyright (c) 2025 MASUTANI Yasuhiro  
All rights reserved.  
This project is licensed under the Apache License 2.0 license found in the LICENSE file in the root directory of this project.

## References

- [rclpy Actions](https://docs.ros2.org/foxy/api/rclpy/api/actions.html)
- [Understanding actions](https://docs.ros.org/en/humble/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Actions/Understanding-ROS2-Actions.html)
- [Writing an action server and client (Python)](https://docs.ros.org/en/humble/Tutorials/Intermediate/Writing-an-Action-Server-Client/Py.html)
  - Does not explain cancellation or accepting new goals during execution.
- [Porting ROS1 SimpleActionServer to ROS2](https://qiita.com/nasu_onigiri/items/783d7ee77556528e5a52)
- [minimal_action_server package](https://github.com/ros2/examples/tree/humble/rclpy/actions/minimal_action_server)
  - Server that handles one goal at a time: [server_single_goal](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_single_goal.py)
  - Server that queues accepted goals: [server_queue_goals](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_queue_goals.py)
  - Server that processes multiple goals concurrently: [server](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server.py)
  - Server that defers and concurrently processes multiple goals: [server_defer](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_defer.py)
  - Server without creating a node class: [server_not_composable](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_server/examples_rclpy_minimal_action_server/server_not_composable.py)
- [minimal_action_client package](https://github.com/ros2/examples/tree/humble/rclpy/actions/minimal_action_client)
  - Minimal client: [client](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client.py)
  - Client that sends a cancel after sending a goal: [client_cancel](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client_cancel.py)
  - Asynchronous client: [client_asyncio](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client_asyncio.py)
  - Client without creating a node class: [client_not_composable](https://github.com/ros2/examples/blob/humble/rclpy/actions/minimal_action_client/examples_rclpy_minimal_action_client/client_not_composable.py)
