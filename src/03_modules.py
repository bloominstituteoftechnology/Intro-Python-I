"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# import os
import os
import sys

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

for i in sys.argv[0]:
    print(i)

# Print out the OS platform you're using:
# YOUR CODE HERE

print(os.name)

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html


# Print the current process ID
# YOUR CODE HERE


print("Current Process ID")
print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Working Directory")
print(os.getcwdb())

# Print out your machine's login name
# YOUR CODE HERE

print("Login Name")
print(os.getlogin())
