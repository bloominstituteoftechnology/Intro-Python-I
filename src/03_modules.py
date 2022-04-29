"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("My command line arguments are:")
for rg in sys.argv:
    print(rg)

# Print out the OS platform you're using:
print("Local platform is: ", sys.platform)

# Print out the version of Python you're using:
print("Local python version is: ", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current process id is: ", os.getpid())

# Print the current working directory (cwd):
print("Current working directory is: ", os.getcwd())

# Print out your machine's login name
print("Current current logged in user: ", os.getlogin())
