"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
def print_argv():

    for argument in sys.argv:
        print(f"argv-argument: {argument}")

# Print out the OS platform you're using:
def print_os_plat():

    print(f"OS platform: {sys.platform}")

# Print out the version of Python you're using:
def print_python_vers():

    print(f"Python version: {sys.version_info}")


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
def print_curr_proc_id():

    print(f"Process ID: {os.getpid()}")

# Print the current working directory (cwd):
def print_cwd():

    print(f"Current Working Directory: {os.getcwd()}")

# Print out your machine's login name
def print_log_name():

    print(f"Login Name: {os.getlogin()}")

if __name__ == "__main__":
    print_argv()
    print_os_plat()
    print_python_vers()
    print_curr_proc_id()
    print_cwd()
    print_log_name()
