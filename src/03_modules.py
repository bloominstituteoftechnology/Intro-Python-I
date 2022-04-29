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
print("Command Line Arguments:")
for clArg in sys.argv:
    print(clArg)
print() #print a carriage return/new line

# Print out the OS platform you're using:
# YOUR CODE HERE
print(f"OS Platform: { sys.platform }\n")

# Print out the version of Python you're using:
# YOUR CODE HERE
print(f"Python Version: { sys.version }\n")


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(f"OS Process ID: { os.ctermid() }\n")

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f"Current Working Directory: { os.getcwd() }\n")

# Print out your machine's login name
# YOUR CODE HERE
print(f"Currently logged in ID: { os.getlogin() }\n")