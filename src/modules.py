"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
arguements = [arg for arg in sys.argv]

# Print out the OS platform you're using:
platform = sys.platform

# Print out the version of Python you're using:
python_version = sys.version

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
proc_id = os.getpid()

# Print the current working directory (cwd):
cwd = os.getcwd()

# Print out your machine's login name
login_name = os.getlogin()


if __name__ == "__main__":
    for i, arg in enumerate(arguements):
        print(f'Arguments{i}: {arg}')

    print('---------------------')
    print(f'Operating System: {platform}')
    print('---------------------')
    print(f'Python Version: {python_version}')
    print('---------------------')
    print(f'Current Process ID: {proc_id}')
    print('---------------------')
    print(f'CWD: {cwd}')
    print('---------------------')
    print(f'Login Name: {login_name}')
    print('---------------------')
