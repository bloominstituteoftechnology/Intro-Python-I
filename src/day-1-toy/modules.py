import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:


# Print out the platform from sys:
print('platform', (sys.platform))

# Print out the Python version from sys:
print('version', (sys.version))



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('process ID', (os.getpid()))

# Print the current working directory (cwd):
print('current directory', os.getcwd())

# Print your login name
print('login name', os.getlogin())

