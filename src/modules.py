import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for x in sys.argv:
    print("argument:\t\t" + x)
# Print out the plaform from sys:
# print(sys.argv)

    
# Print out the Python version from sys:
print("Python Version:\t\t" + sys.version)



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Process ID:\t\t" + str(os.getpid()))

# Print the current working directory (cwd):
print("Working Directory:\t" + str(os.getcwd()))

# Print your login name
print("Current User:\t\t" + str(os.getlogin()))

