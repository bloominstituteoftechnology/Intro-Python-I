"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for index, arg in enumerate(sys.argv):
    print(f"Command line argument #{index + 1}: {arg}")

# Print out the OS platform you're using:
# YOUR CODE HERE
print(f"OS platform: {sys.platform}")

# Print out the version of Python you're using:
# YOUR CODE HERE
print(f"Python version: {sys.version}")
import platform
print(f"Python version: {platform.python_version()}")

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f"Current process ID: {os.getpid()}")

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f"Current working directory: {os.getcwd()}")

# Print out your machine's login name
# YOUR CODE HERE
loginName = os.getlogin()

if loginName != "root":
    print(loginName)
else:
    import getpass
    print(f"Computer login name: {getpass.getuser()}")
