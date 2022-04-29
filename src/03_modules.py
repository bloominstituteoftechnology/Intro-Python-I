"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
# * SOLUTIONS BELOW:
# * OPEN INTERPRETER && RUN: python3 03_modules.py

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for argument in dir(sys.argv): print("Argument: ", argument)

# Print out the OS platform you're using:
print('PLATFORM :', sys.platform)

# Print out the version of Python you're using:
print('IMPLEMENTATION VERSION INFORMATION', sys.implementation)
print('VERSIONS INFORMATION: ', sys.version_info)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('CURRENT PROCESS ID: ', os.getpid())

# Print the current working directory (cwd):
print('CURRENT WORKING DIRECTORY (CWD): ', os.getcwd())

# Print out your machine's login name
print('CURRENT LOCAL MACHINE LOGIN NAME: ', os.getlogin())
