import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
#???
# import fileinput
# for line in fileinput.input():
#     process(line)
# for line in fileinput.input(sys.argv):
#     process(line)
# for arg in sys.argv:
#     print(arg)


# Print out the platform from sys:
# print()
print(sys.platform)

# Print out the Python version from sys:
# print()
print(sys.version)



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# print()
print(os.getpid())

# Print the current working directory (cwd):
# print()
print(os.getcwd())

# Print your login name
# print()
print(os.getlogin())

