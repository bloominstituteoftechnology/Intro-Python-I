import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
    print(arg)
# Print out the plaform from sys:
print(sys.platform)

# Print out the Python version from sys:
print(sys.version)



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("PROCESS ID BELOW: ")
process = os.getgid()
print(process)


# Print the current working directory (cwd):
print("CWD BELOW: ")
cwd = os.getcwd()
print(cwd)

# Print your login name
print("LOGIN NAME BELOW :")
my_login_name = os.getlogin()
print(my_login_name)