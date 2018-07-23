import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
  print(arg)

# Print out the plaform from sys:
print("sys platform: ", sys.platform)

# Print out the Python version from sys:
major = sys.version_info.major
minor = sys.version_info.minor
micro = sys.version_info.micro
print("python version: %d.%d.%d" % (major, minor, micro))



# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
currentProcessID = os.getpid()
print(currentProcessID)

# Print the current working directory (cwd):
currentWorkingDirectory = os.getcwd()
print(currentWorkingDirectory)

# Print your login name
loginName = os.getlogin()
print(loginName)