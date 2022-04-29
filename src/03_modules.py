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
print("this is the output of sys.argv[0]", sys.argv[0])
# Print out the OS platform you're using:
# YOUR CODE HERE
print("this is the operating system that i'm using", sys.platform)
# Print out the version of Python you're using:
# YOUR CODE HERE
print("This is the version of python i'm running", sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
# print("this is the process id that i'm currently using", os.getegid() ) these commands are unix exclusive they won't work in windows
# print("or maybe this one is the process id that i'm currently using", os.geteuid() )
print("This is the process id", os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("This is the current working directory", os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print("this is my machine's login name", os.getlogin())
