"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os
import getpass
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("⚠️⚠️⚠️⚠️⚠️This is the name of the script: ", sys.argv[0])
print("⚠️⚠️⚠️⚠️⚠️Number of arguments: ", len(sys.argv))
print("⚠️⚠️⚠️⚠️⚠️The arguments are: ", str(sys.argv))

print(f"{sys.builtin_module_names}")
# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
# Print out the OS platform you're using:
# YOUR CODE HERE
print("⚠️⚠️⚠️⚠️⚠️⚠️the os on the system is:", (os.environ))
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Print the current process ID
# YOUR CODE HERE
id = os.getpid

os = dir_path = os.path.dirname(os.path.realpath(__file__))
print(os)


# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE

getpass.getuser()
