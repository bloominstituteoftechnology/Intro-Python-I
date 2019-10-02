"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

def cs_argv():
    argv = []
    for a in sys.argv:
        argv.append(a)

    return argv

argv = cs_argv() 
print(argv)

# Print out the OS platform you're using:
# YOUR CODE HERE
def cs_platform():
    platform = sys.platform
    print(platform)

# cs_platform()

# Print out the version of Python you're using:
# YOUR CODE HERE

def cs_version():
    version = sys.version
    print(version)

# cs_version()


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

def cs_getpid(): 
    getpid = os.getpid()
    print(getpid)

# cs_getpid()

# Print the current working directory (cwd):
# YOUR CODE HERE
def cs_getcwd():
    return os.getcwd()

# print(cs_getcwd())

# Print out your machine's login name
# YOUR CODE HERE

def cs_loginname():
    return os.getlogin()

# print(cs_loginname())