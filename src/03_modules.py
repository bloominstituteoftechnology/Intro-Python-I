"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for argument in sys.argv:
    print(argument)

# or this if you don't want the script name:
for i in range(1, len(sys.argv)):
    print(sys.argv[i])

# Print out the OS platform you're using:
print(sys.platform)

# Print out the version of Python you're using:
print(sys.version) # version plus extra info

# this is the version you'd want to check against:
version = sys.version_info
print(f"{version.major}.{version.minor}.{version.micro}")

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpid())

# Print the current working directory (cwd):
print(os.getcwd())

# Print out your machine's login name
print(os.getlogin())

# documentation says this is more reliable:
import getpass
print(getpass.getuser())