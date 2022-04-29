"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# 3
# https://github.com/LambdaSchool/Intro-Python-I/blob/master/src/03_modules.py

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
for arg in sys.argv:
   print ("list of command line arguments passed to a Python script:", sys.argv)


# Print out the OS platform you're using:
print("operating system:", sys.platform)

# Print out the version of Python you're using:
print ("python version:", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("current process id:", os.getpid())
print("parent process id:", os.getppid())

# Print the current working directory (cwd)
print("current working directory:", os.getcwd())

# Print out your machine's login name
# doesn't work on colab
#print("login name:", os.getlogin())


