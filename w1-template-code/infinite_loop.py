import time
import os
import sys


def main() -> None:
    # Repeat the loop 40 times
    count = 40
    sleep = 1    # Modify this value to change the sleep duration

    # Grab the current process ID
    pid = os.getpid()
    # Stop the infinite loop after count reaches 0
    while count > 0:
        # Print process details
        print("{:.03f}: {} This is an infinite loop.".format(time.time(), pid))
        time.sleep(sleep)  # Put the process to sleep for 'sleep' seconds
        count -= 1  # Decrement the remaining iterations


if __name__ == "__main__":
    main()
