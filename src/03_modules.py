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
for arg in sys.argv:
    print(arg) 
  
# Print out the OS platform you're using:
# YOUR CODE HERE
import platform 
print(platform.system())

# Print out the version of Python you're using:
# YOUR CODE HERE
print(platform.python_version())

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
pid = os.getpid()
print(pid)

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print(cwd)

# Print out your machine's login name
# YOUR CODE HERE
login_name = os.getlogin()
print(login_name)
