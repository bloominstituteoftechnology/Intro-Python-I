"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

print("sys.argv command line arguments, one per line:")
print(sys.argv, '\n')

print("OS platform:")
print(sys.platform, '\n')

print("Python version:")
print(sys.version, '\n')


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

print("current process ID:")
print(os.getpid(), '\n')

print("current working directory (cwd):")
print(os.getcwd(), '\n')

print("machine's login name:")
print(os.getlogin(), '\n')
