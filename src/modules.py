"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print(sys.argv)           # ['modules.py']

# Print out the OS platform you're using:
print(sys.platform)       # darwin

# Print out the version of Python you're using:
print(sys.version_info)   # sys.version_info(major=3, minor=7, micro=2, releaselevel='final', serial=0)
print(sys.version)        #3.7.2 (default, Dec 27 2018, 07:35:52)
                          # [Clang 10.0.0 (clang-1000.11.45.5)]

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpid())

# Print the current working directory (cwd):
print(os.getcwd())

# Print out your machine's login name
print(os.getlogin())