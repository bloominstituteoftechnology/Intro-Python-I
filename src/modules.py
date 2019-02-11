"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print out the command line arguments in sys.argv, one per line:
print('-- Being Arguments --------')
for argument in sys.argv:
    print(argument)
print('-- End Arguments ----------\n')

# Print out the OS platform you're using:
print('OS: '+os.name)

# Print out the version of Python you're using:
print('Version: '+sys.version)

# Print the current process ID
print('Process ID: '+str(os.getpid()))

# Print the current working directory (cwd):
print('Working Directory: '+os.getcwd())

# Print out your machine's login name
print('Login Name: '+os.getlogin())
