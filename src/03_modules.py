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
  print(arg)          #print path of the file

# Print out the OS platform you're using:
# YOUR CODE HERE

print(sys.platform)   #print win32

# Print out the version of Python you're using:
# YOUR CODE HERE

print(sys.version)    #print 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)]

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print(os.getpid())        #print number

# Print the current working directory (cwd):
# YOUR CODE HERE

print(os.getcwd())        #print current directory name

# Print out your machine's login name
# YOUR CODE HERE

print(os.getlogin())      #print Penny
