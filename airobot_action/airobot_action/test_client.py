import os
import sys
import readline  # Required to add history support to input()
import threading
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.utilities import remove_ros_args
from action_msgs.msg import GoalStatus
from airobot_interfaces.action import StringCommand


class TestClient(Node):
    def __init__(self, action_name):
        super().__init__('test_client')
        self.get_logger().info(f'Starting client for {action_name}')
        self.goal_handle = None  # Variable to store active goal info
        self.action_client = ActionClient(
            self, StringCommand, action_name)
        while not self.action_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info('Action server unavailable, waiting...')

    def send_goal(self, command):
        self.get_logger().info(f'Sending goal: {command}')
        goal_msg = StringCommand.Goal()
        goal_msg.command = command
        self.send_goal_future = self.action_client.send_goal_async(
            goal_msg, feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Feedback: \'{feedback_msg.feedback.process}\'')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal was rejected')
            return
        self.goal_handle = goal_handle  # Update goal info
        self.get_logger().info('Goal accepted')
        self.get_result_future = goal_handle.get_result_async()
        self.get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info(f'Result: {result.answer}')
        else:
            self.get_logger().info(f'Failure status: {status}')
        self.goal_handle = None  # Reset goal info

    def cancel(self):
        if self.goal_handle is None:
            self.get_logger().info('Nothing to cancel')
            return
        self.get_logger().info('Cancel')
        future = self.goal_handle.cancel_goal_async()
        future.add_done_callback(self.cancel_done)

    def cancel_done(self, future):
        cancel_response = future.result()
        if len(cancel_response.goals_canceling) > 0:
            self.get_logger().info('Cancel succeeded')
            self.goal_handle = None  # Reset goal info
        else:
            self.get_logger().info('Cancel failed')


def main():
    action_name = 'command'                # Default action name
    args = remove_ros_args(args=sys.argv)  # Remove ROS args from command line
    if len(args) >= 2:                     # Use the 1st arg as action name
        action_name = args[1]
    history_path = '.history' + '_' + action_name.replace('/', '_')
    if os.path.isfile(history_path):
        readline.read_history_file(history_path)
    print('''Usage:
  Type a string + Enter -> Send as StringCommand goal command
  Enter -> Cancel
  exit + Enter -> Exit program
  You can send the next goal while the server is running
  Line history and line editing supported''')

    rclpy.init()
    node = TestClient(action_name)
    thread = threading.Thread(target=rclpy.spin, args=(node,))
    threading.excepthook = lambda x: ()
    thread.start()

    try:
        while True:
            command = input('command: ')
            if command == '':        # Pressing only Enter cancels
                node.cancel()
            elif command == 'exit':  # Exit on 'exit'
                break
            else:                    # Otherwise, send the string as a goal
                node.send_goal(command)
    except KeyboardInterrupt:
        pass

    rclpy.try_shutdown()

    readline.write_history_file(history_path)
