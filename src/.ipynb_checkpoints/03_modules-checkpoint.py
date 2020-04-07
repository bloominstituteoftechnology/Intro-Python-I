"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('Command line arguments:')
for arg in sys.argv:
    print(arg)

# Print out the OS platform you're using:
print('OS:', sys.platform, sys.getwindowsversion().platform_version)

# Print out the version of Python you're using:
s = sys.version_info
print(f'Python v{s.major}.{s.minor}.{s.micro}')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'Process ID: {os.getpid()}')

# Print the current working directory (cwd):
print(f'Directory: {os.getcwd()}')

# Print out your machine's login name
print(f'User: {os.getlogin()}')
