"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv)

# Print out the OS platform you're using:
# YOUR CODE HERE
if sys.platform.startswith("linux"):
    print("You are on a Linux Machine")
elif sys.platform.startswith("darwin"):
    print("You are using a Mac Machine")
elif sys.platform.startswith("win30"):
    print("You need an upgrade")
else:
    print("You are a caveman")

    # Print out the version of Python you're using:
    # YOUR CODE HERE
print('Your current version of Python is: ' + sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('Your current process user id is: ' + str(os.geteuid()) +
      '. The current group id is: ' + str(os.getgid()) + '.')

# Print the current working directory (cwd):
# YOUR CODE HERE
print('The working directory is: ' + str(os.getcwd()))

# Print out your machine's login name
# YOUR CODE HERE
print('Your login name is: ' + str(os.getlogin()))
