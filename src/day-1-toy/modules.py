import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:

# sys.argv:  The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, argv[0] is the empty string.
for i in sys.argv:
    print(i)

# Print out the platform from sys:
# 
# sys.platform: This string contains a platform identifier that can be used to append platform-specific components to sys.path, for instance.
print(sys.platform)

# Print out the Python version from sys:
print(sys.version_info)



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpid())

# Print the current working directory (cwd):
print(os.getcwd())

# Print your login name
print(os.getlogin())

