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
print(sys.platform)

# print(sys.getwindowsversion()[0])

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
print(sys.version_info)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
print(os.getpgid(os.getpid()))

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE

# os.getlogin() isn't working on my machine. Might be bc I'm using python3.6.2
# print(os.getlogin())
# found this referenced in the docs for os.getlogin()
import pwd
print(pwd.getpwuid(os.getuid())[0])