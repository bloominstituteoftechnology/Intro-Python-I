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
print("This is the name of the script:", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are:", str(sys.argv))

# Print out the OS platform you're using:
# YOUR CODE HERE
print("The OS platform i'm using is", sys.platform) #darwin

# Print out the version of Python you're using:
# YOUR CODE HERE
print("The version of Python i'm using is:", sys.version)
print("The sys.prefix is", sys.prefix)
print("The sys.api_version is", sys.api_version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("The current process ID:", os.getpgid(0))

# Print the current working directory (cwd):
# YOUR CODE HERE
print("The current working directory is:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("Your machine's login name is:", os.getlogin())

import getpass
print("getpass.getuser() is another way to get the login name:", getpass.getuser())