import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
    print(f"{arg}")

# Print out the platform from sys:
print("System Platform!!")
print(sys.platform)

# Print out the Python version from sys:
print(sys.version)



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("PID")
print(os.getpid())

# Print the current working directory (cwd):
print("Current Working Directory")
print(os.getcwd())

# Print your login name
print("Login")
print(os.getlogin())

