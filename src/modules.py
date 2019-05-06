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
for item in sys.argv:
print(item)
['']

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)
'darwin'

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
'3.7.2 (default, Dec 27 2018, 07:35:52) \n[Clang 10.0.0 (clang-1000.11.45.5)]'


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
os.getpid()
42877

# Print the current working directory (cwd):
# YOUR CODE HERE

os.getcwd()
'/Users/josephbradley'



# Print out your machine's login name
# YOUR CODE HERE
