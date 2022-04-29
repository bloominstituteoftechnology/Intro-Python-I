"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
sys.argv[0]

# Print out the OS platform you're using:
import os
print(os.name)

# Print out the version of Python you're using:
#From terminal
print(sys.version)
print('Python version: Python 3.8.2')

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
os.getpid()

# Print the current working directory (cwd):
os.getcwd()

# Print out your machine's login name
os.uname().nodename