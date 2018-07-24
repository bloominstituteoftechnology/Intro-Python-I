import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
    print(f'CL argument: {arg}')

# Print out the plaform from sys:
print(f'platform: {sys.platform}')

# Print out the Python version from sys:
print(f'Python version: {sys.version}')

# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'current ID: {os.getgid()}')

# Print the current working directory (cwd):
print(f'current working directory: {os.getcwd()}')

# Print your login name
print(f'name of the user: {os.getlogin()}')

