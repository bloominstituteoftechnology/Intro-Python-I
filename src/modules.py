import sys
import os
import getpass

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for argv in sys.argv:
    print(argv)

# Print out the plaform from sys:
print("\nPlatform:\n", sys.platform)

# Print out the Python version from sys:
print("\nPython Version:\n", sys.version)



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("\nCurrent Process ID:\n", os.getpid())

# Print the current working directory (cwd):
print("\nCurrent Working Directory:\n", os.getcwd())

# Print your login name
print("\nLogin name:\n", getpass.getuser()) # Preferred method to get login name from getpass module
print("\nLogin name:\n", os.getlogin()) 

