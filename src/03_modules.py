"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# if len(sys.argv) > 1:
#     for arg in sys.argv:
#         print(arg)
# else:
#         print('No arguments provided.')

# Print out the OS platform you're using:
# import platform
# import os

# print('The os is ' + str(os.name) + ',')
# print('and the platform is ' + str(platform.system()) + '.')



# Print out the version of Python you're using:
#print('This version of Python is:  ' + str(sys.version))



import os
import getpass
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('The current process ID is ' + str(os.geteuid()) + '.')

# Print the current working directory (cwd):
print('The current working directory is: ' + str(os.getcwd()))

# Print out your machine's login name
print(getpass.getuser())
