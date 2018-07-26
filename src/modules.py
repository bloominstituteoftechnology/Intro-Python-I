import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:


# Print out the plaform from sys:
# for arg in sys.argv:
#     print(arg)


# Print out the Python version from sys:print(sys.platform)
# print(sys, sep="\n", sys.path)
print("platform: "+sys.platform + "\n" + "maxsize: "+str(sys.maxsize) + "\n" + "argv: "+str(sys.argv))




# # Module "os"
# #
# # See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# # Print the current process ID
print("Process ID: "+ str(os.getpid()) + "\n" + "cwd: " + os.getcwd() + "\n" + "login id: " + os.getlogin())

# # Print the current working directory (cwd):
# print()

# # Print your login name
# print()
