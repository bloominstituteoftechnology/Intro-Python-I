"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: c
# sys.stderr.write('"sys.stdout.write()"')
# sys.stdout.write(" is same as print function")
# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# for list in sys.argv:
#     print(list)
if len(sys.argv) > 1:
    print(float(sys.argv[1]) + 5)
# Print out the OS platform you're using:
# YOUR CODE HERE

# Print out the version of Python you're using:
# YOUR CODE HERE


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID

# YOUR CODE HERE

print(os.getppid())
# print(os.getcwd())

# # Print the current working directory (cwd):
# # YOUR CODE HERE
print(os.getcwd())
# print(os.name)
# # Print out your machine's login name
# # YOUR CODE HERE
print(os.getlogin())
# print(os.getpgrp())