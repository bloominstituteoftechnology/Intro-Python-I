"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

print('\n--- sys ---')

# Print out the command line arguments in sys.argv, one per line:
print('\ncommand line arguments:')
for arg in sys.argv:
    print(arg)

# Print out the OS platform you're using:
print('\nplatform:')
print(sys.platform)

# Print out the version of Python you're using:
print('\npython version:')
print(sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

print('\n--- os ---')

# Print the current process ID
print('\ncurrent process ID:')
print(os.getpid())

# Print the current working directory (cwd):
print('\ncurrent working directory:')
print(os.getcwd())

# Print out your machine's login name
print('\ncurrent user:')
print(os.getlogin())
