"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""


# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
"""
Import Statements:
"""

import os
import sys
print('Command Line Arguments:')
([(print(i)) for i in sys.argv], '\n')
print('\n')
# Print out the OS platform you're using:
print('+--------------------------+')
# YOUR CODE HERE
"""
Print statement + "\n" newline
sys.platform is a string that contains a platform
identifier that can be used to append platform-specific components to sys.path,
for instance.

The platform module provides a detail check for the system's identiy.
"""
print('My OS Platform is:\n', sys.platform, '\n')

# Print out the version of Python you're using:

"""
sys.version is a string indicating information on
current version number.
"""
print('+--------------------------+')
# YOUR CODE HERE
print('Python Version:\n', sys.version, '\n')

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID

"""
os.getpid() is a methond used in Python which is used to get the process ID of
the current process.

The return type of this method is of class 'int'.
"""
print('+--------------------------+')
# YOUR CODE HERE
print('My Current Process ID:\n', os.getpid(), '\n')

# Print the current working directory (cwd):
"""
A Python method getcwd() returns current working dicrectory of a process.
e.g, Syntax.
Which is the syntax for getcwd() method - cwd =  os.getcwd()
"""
print('+--------------------------+')
# YOUR CODE HERE
print('My current Working Directory is:\n', os.getcwd(), '\n')
# Print out your machine's login name
"""
os.getlogin(). Returns the name of the user logged in on the controlling
terminal of the process.
"""
print('+--------------------------+')
# YOUR CODE HERE
print("Machine's Login Name is:\n", os.getlogin(), '\n')
