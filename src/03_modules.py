"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for idx,arg in enumerate(sys.argv):
    print("Arg {}: {}".format(idx, arg))

# Print out the OS platform you're using:
print("Platform: {}".format(sys.platform))

# Print out the version of Python you're using:
print("Python version: {}.{}.{} {}-{}".format(*sys.version_info))

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Process ID (pid): {}".format(os.getpid()))

# Print the current working directory (cwd):
print("CWD: {}".format(os.getcwd()))

# Print out your machine's login name
print("Login Name: {}".format(os.getlogin()))
