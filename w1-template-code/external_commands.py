import os


def run_ps():
    pid = os.fork()  # create a child process

    if pid == 0:
        # Child process
        print(f"Child (PID={os.getpid()}): running 'ps -aux'")
        os.execvp("bash", ["bash", "-c", "ps -aux"])
        # execvp replaces the current process, so no code below this line runs in child
    else:
        # Parent process
        print(f"Parent (PID={os.getpid()}): waiting for child (PID={pid})")
        os.wait()  # wait for the child process to finish
        print("Parent: child process finished")


if __name__ == "__main__":
    run_ps()
