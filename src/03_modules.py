"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arguments_ in sys.argv:
  print(f'command line arguements: {arguments_} \n')

# Print out the OS platform you're using:
print(f'OS Platform in use: {sys.platform} \n')

# Print out the version of Python you're using:
print(f'python version: {sys.version} \n')


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'The current process id: {os.getpid()} \n')

# Print the current working directory (cwd):
print(f'The current working directory: {os.getcwd()} \n')

# Print out your machine's login name
print(f'login name: {os.getuid()} \n')

# this should in theory work, but throws the error: no such file or directory.
# it doesn work when using os.getlogin(). 
# print(f'login name: {os.getlogin()} \n')