import sys
# see docs for the sys module: https://docs.python.org/3.7/library/sys.html

# print out the command line arguments in sys.argv, one per line

for line in sys.argv:
    print(line)

# print out the OS platform you're using

print(sys.platform)

# print out the version of Python you're using

print(sys.version)

import os
# see the docs for the OS module: https://docs.python.org/3.7/library/os.html

# print the current process ID

print(os.getpid())

# print the current working directory (cwd):

print(os.getcwd())

# print out your machine's login name

print(os.getlogin())