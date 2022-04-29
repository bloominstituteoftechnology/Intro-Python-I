"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
# Print out the command line arguments in sys.argv, one per line:
arguements = [arg for arg in sys.argv]
for i, arg in enumerate(arguements):
    print(f'Arguments{i}: {arg}')
print()

# Print out the OS platform you're using:
OS_platform = sys.platform
print(f'Operating System: {OS_platform}')
print()

# Print out the version of Python you're using:
python_version = sys.version
print(f'Python Version: {python_version}')
print()

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Print the current process ID
process_ID = os.getpid()
print(f'Current Process ID: {process_ID}')
print()

# Print the current working directory (cwd):
current_dir = os.getcwd()
print(f'CWD: {current_dir}')
print()

# Print out your machine's login name
name = os.getlogin()
print(f'Login Name: {name}')
print()
