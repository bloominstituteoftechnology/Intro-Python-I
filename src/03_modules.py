"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

#  Print out the command line arguments in sys.argv, one per line:

print('The script has the name %s' % (sys.argv[0]))

arguments = len(sys.argv) - 1
position = 1
while (arguments >= position):
    print ('Parameter %i: %s' % (position, sys.argv[position]))
    position = position + 1

# Print out the OS platform you're using:
print(f'The current OS platform I am using is: {sys.platform}')

# Print out the version of Python you're using:
import platform
print(f'The current python version I am using is: {platform.python_version()}')


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'The current process ID is: {os.getpid()}')

# Print the current working directory (cwd):
print(f'My current working directory is: {os.getcwd()}')

# Print out your machine's login name
print(f'My machines login name is: {os.getlogin()}')
