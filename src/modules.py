import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:


# Print out the plaform from sys:
print(sys.platform, sys.argv)

# Print out the Python version from sys:
print(sys.version_info, sys.argv)



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpid(), sys.argv)

# Print the current working directory (cwd):
print(os.getcwd(), sys.argv)

# Print your login name
print(os.getlogin(), sys.argv)

