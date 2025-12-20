import time, random
from threading import Lock
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor
from airobot_interfaces.action import StringCommand  # Import custom action definition


class BringmeActionServer(Node):
    def __init__(self):
        super().__init__('bringme_action_server')
        self.goal_handle = None    # Variable to store the active goal info
        self.goal_lock = Lock()    # Lock to avoid double execution
        self.execute_lock = Lock() # Lock to avoid double execution
        self._action_server = ActionServer(
            self, StringCommand, 'command', 
            execute_callback=self.execute_callback,
            cancel_callback=self.cancel_callback,
            handle_accepted_callback=self.handle_accepted_callback,
            callback_group=ReentrantCallbackGroup(),
        )
        self.food = ['apple', 'banana', 'candy']

    def handle_accepted_callback(self, goal_handle):
        with self.goal_lock:                # Avoid double execution in this block
            if self.goal_handle is not None and self.goal_handle.is_active:
                self.get_logger().info('Abort previous process')
                self.goal_handle.abort()
            self.goal_handle = goal_handle  # Update goal info
        goal_handle.execute()               # Execute goal

    def execute_callback(self, goal_handle):
        with self.execute_lock:            # Avoid double execution in this block
            feedback = StringCommand.Feedback()
            result = StringCommand.Result()
            count = random.randint(5, 10)

            while count > 0:
                if not goal_handle.is_active:
                    self.get_logger().info('Abort process')
                    return result

                if goal_handle.is_cancel_requested:
                    self.get_logger().info('Cancel process')
                    goal_handle.canceled()
                    return result

                self.get_logger().info(f'Sending feedback: {count}[s] left')     
                feedback.process = f'{count}'
                goal_handle.publish_feedback(feedback)  
                count -= 1  
                time.sleep(1)

            item = goal_handle.request.command
            if item in self.food:
                result.answer = f'Yes, here is {item}'
            else:
                result.answer = f'Could not find {item}'
            goal_handle.succeed()
            self.get_logger().info(f'Goal result: {result.answer}')
            return result

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Cancel received')
        return CancelResponse.ACCEPT


def main():
    rclpy.init()
    bringme_action_server = BringmeActionServer()
    print('Server started')
    try:
        rclpy.spin(bringme_action_server, executor=MultiThreadedExecutor())
    except KeyboardInterrupt:
        pass
    rclpy.try_shutdown()
    print('Server stopped')
