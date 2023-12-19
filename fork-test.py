import os
import time

def child_process():
    print("This is the child process.")
    time.sleep(5)  # Sleep for demonstration purposes
    print("Child process exiting.")

def parent_process():
    print("This is the parent process.")
    time.sleep(5)  # Sleep for demonstration purposes
    print("Parent process exiting.")

pid = os.fork()

if pid == 0:
    # Child process
    child_process()
else:
    # Parent process
    parent_process()
