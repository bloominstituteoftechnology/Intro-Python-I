"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os
import getpass
import platform

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for x in sys.argv:
    print(str(x))

# Print out the OS platform you're using:

print(os.uname())

if os.name == "posix":
    print(os.system("uname -a"))
else:
    print("unknown OS")
# Print out the version of Python you're using:
print(sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# Print out your machine's login name
print(getpass.getuser())
# YOUR CODE HERE
