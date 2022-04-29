"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

modules = []

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
argv = []
for i in dir(sys.argv):
    argv.append(i)

modules.append(argv)

# Print out the OS platform you're using:
# YOUR CODE HERE
platform = sys.platform
modules.append(platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
version = sys.version
modules.append(version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
processid = os.getpid()
modules.append(processid)

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
modules.append(cwd)

# Print out your machine's login name
# YOUR CODE HERE
machinelogin = os.getlogin()
modules.append(machinelogin)

for i in modules:
    if type(i) == list:
        for _ in i:
            print(_)
    else:
        print(i)