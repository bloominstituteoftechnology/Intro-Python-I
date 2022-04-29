"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for argument in sys.argv:
    print("Command line arguments: " + str(argument))

# Print out the OS platform you're using:
# YOUR CODE HERE
print("Platform: " + str(sys.platform)) #There isn't a good way to do this on Mac.  See next lines
for attribute in os.uname():
    print(attribute)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Version: " + str(sys.version))



# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Process ID: " + str(os.getpid()))

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current working directory: " + str(os.getcwd()))

# Print out your machine's login name
# YOUR CODE HERE
import getpass
print("Login name: " + str(getpass.getuser())) #The os.getlogin() doesn't work correctly on my Mac.