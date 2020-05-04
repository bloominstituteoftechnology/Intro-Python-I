"""
In this exercise, you'll be playing around with 

- the sys module, which allows you to access many system 
specific variables and methods, and 

- the os module, which gives you access to lower-level 
operating system functionality.
"""

import sys
import os

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
args = sys.argv
print(type(sys.argv))
      
arg_count = len(args)
print(f'The number of sys.argvs returned is: {arg_count}')
if len(args) > 0:
    for i, val in enumerate(args):
         print(f"arg[{i}]: {val}")
else:
    print("<None to list>")
    


# Print out the OS platform you're using:
# YOUR CODE HERE


print("os.name returns " + os.name)
print("sys.platform returns " + sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
    
# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())


# Print out your machine's login name
# YOUR CODE HERE
print(os.uname()[1])
