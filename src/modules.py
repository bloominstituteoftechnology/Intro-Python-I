import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for index,item in enumerate(sys.argv):
    print('Arg number(%i):\t\t\t%s'%(index, item))

# Print out the plaform from sys:
print('The Current Platform is:\t%s'%sys.platform)

# Print out the Python version from sys:
print('The Current Version is:\t\t%s'%sys.version)

# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('The Current Process ID is:\t%s'%os.getpid())

# Print the current working directory (cwd):
print('The Current Working Directory:\t%s'%os.getcwd())

# Print your login name
print('The Current User is:\t\t%s'%os.getlogin())

