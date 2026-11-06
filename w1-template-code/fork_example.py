import os
import time
import signal


child_finished = False


def sigchild_handler(signum, frame):
    global child_finished
    print("Child process terminated.")
    child_finished = True


# Create a child process. The parent process receives the child's PID, while the child process receives 0.
pid = os.fork()

if pid > 0:
    # This is the parent process
    print("Parent process PID: {}".format(os.getpid()))
    print("Child process PID from parent process: {}".format(pid))
    # Wait for the child process to finish
    # os.wait() can replace this block code  to block the parent process
    # until the child process terminates.
    signal.signal(signal.SIGCHLD, sigchild_handler)  # Prevent zombie processes
    while True:
        if child_finished:
            break
        time.sleep(1)
    print("Parent process has finished.")
else:
    # This is the child process
    print("Child process PID: {}".format(os.getpid()))
    for i in range(20):
        print("Child process is running... {}".format(i))
        time.sleep(1)
    print("Child process is exiting.")
