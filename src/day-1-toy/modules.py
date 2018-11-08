import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print(sys.argv[0], "= script name")

# Print out the platform from sys:
print(sys.platform, "= platform name")

# Print out the Python version from sys:
print(sys.version, "= version of Python")



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpid(), "= process id")

# Print the current working directory (cwd):
print(os.getcwd(), "= current working directory")

# Print your login name
print(os.getlogin(), "= login name")

