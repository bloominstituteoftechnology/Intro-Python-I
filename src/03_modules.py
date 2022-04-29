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

for argument in sys.argv:
    print(argument)

# Print out the OS platform you're using:
import platform
import os
print(platform.system())

# Print out the version of Python you're using:
print(sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
pid = os.getpid()
print(pid)


# Print the current working directory (cwd):
path = os.getcwd()
print(path)

# Print out your machine's login name
import getpass
user = getpass.getuser()
print(user)
