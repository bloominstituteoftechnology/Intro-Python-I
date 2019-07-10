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

print(f"Your system platform: {sys.platform}")


# Print out the version of Python you're using:
# YOUR CODE HERE


v = sys.version_info
print('Python version {}.{}.{}'.format(*v))


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

v = os.name
p = os.getenv('PATH')
d = os.getcwd()
r = os.urandom(25).hex()
pid = os.getpgid()
login = os.getlogin()
print(f'Operating System: {v}')
print(f'PATH: {p}')
print(f'Random hexadecimal number from OS: {r}')

# Print the current process ID
# YOUR CODE HERE
print(f'Process ID: {pid}')

# Print the current working directory (cwd):
# YOUR CODE HERE
print(f'Current working directory: {d}')

# Print out your machine's login name
# YOUR CODE HERE
print(f"This machine's login name: {login}")