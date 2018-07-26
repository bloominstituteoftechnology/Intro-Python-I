import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:


# Print out the plaform from sys:
print('platform: ',sys.getwindowsversion().platform)

# Print out the Python version from sys:
print("python version is: {}.{}".format(sys.version_info.major, sys.version_info.minor))



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('Process id:',os.getpid())

# Print the current working directory (cwd):
print('current working directory: ', os.getcwd())

# Print your login name
print('log in name: ', os.getlogin())

