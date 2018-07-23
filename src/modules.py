import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print(sys.argv) # returns list of command line args passed to script
for arg in sys.argv:
	print(arg);

# Print out the plaform from sys:
print("platform on this machine is", sys.platform)

# Print out the Python version from sys:
print("current Python version is", sys.version_info)
print("major part of Python version number is", sys.version_info.major)
print("minor part of Python version number is", sys.version_info.minor)
print("micro part of Python version number is", sys.version_info.micro)
print("releaselevel part of Python version number is", sys.version_info.releaselevel)
print("serial part of Python version number is", sys.version_info.serial)

# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print()

# Print the current working directory (cwd):
print()

# Print your login name
print()

