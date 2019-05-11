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
for x in range(len(sys.argv)):
    print('command line', sys.argv[x])

# Print out the OS platform you're using:
# YOUR CODE HERE
print('OS', sys.platform)
# print "This is the name of the script: ", sys.argv[0]
x = sys.argv[0]
print ("This is the name of the script: {} " .format(x) )
# Print out the version of Python you're using:
# YOUR CODE HERE
y = sys.version
print ("This is the version of Python I am using: {} " .format(y) )



import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
id = os.getpid()

print ("This is the process id: {} " .format(id) )


# Print the current working directory (cwd):
# YOUR CODE HERE
wd = os.getcwd()
print ("This is the working directory: {} " .format(wd) )


# Print out your machine's login name
# YOUR CODE HERE

lin = os.getlogin()
print ("This is the login name: {} " .format(lin) )


