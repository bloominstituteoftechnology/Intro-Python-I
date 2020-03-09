"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("The command line arguments in sys.argv are:")
for i in sys.argv:
    print(i)

# Print out the OS platform you're using:
print(f'The OS platform is: {sys.platform}')

# Print out the version of Python you're using:
print(f'The system version is: {sys.version}')


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'The current process ID is: {os.getpid()}')

# Print the current working directory (cwd):
print(f'The CWD is: {os.getcwd()}')

# Print out your machine's login name
print(f'The login name is: {os.getlogin()}')
