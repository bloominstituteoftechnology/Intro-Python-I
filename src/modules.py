"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# bash-3.2$ python src/modules.py

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for each in sys.argv:
    print(each)
# Output: src/modules.py

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)
# Output: darwin

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
# Output: 3.7.2 (default, Jan 13 2019, 12:50:15) [Clang 10.0.0 (clang-1000.11.45.5)]

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
# Output: 89894

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# Output: /Users/sarahtennis/Desktop/python/Intro-Python-I

# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())
# Output: sarahtennis
