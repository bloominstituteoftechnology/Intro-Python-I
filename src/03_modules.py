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
# total arguments
n = len(sys.argv)

print("\nName of Script: ", sys.argv[0])
print("\nArguments Passed:", end = " ")
# since first element is name of script, we start at index 1 
for i in range(1, n):
	print(sys.argv[i], end = " ")
# Print out the OS platform you're using:
# YOUR CODE HERE
print("\nThe version of Windows is: ")
print(sys.getwindowsversion())

# Print out the version of Python you're using:
# YOUR CODE HERE
print("\nThe version of Python is: ")
print(sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
# other 2 versions only work in unix
print("\n The process ID is: ")
print(os.getppid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print("\n The CWD is: ")
print(os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("\n The Login Name is: ")
print(os.getlogin())