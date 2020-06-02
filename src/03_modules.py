"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print('sys.argv command line arguments: ')
for i in range(0, len(sys.argv)):
    print(sys.argv[i])

# Print out the OS platform you're using:
# YOUR CODE HERE
print('i am using this platform: ' + sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
python_path = sys.exec_prefix  # path to my python file
print(python_path.split("/"))  # split the characters into a list
print(len(python_path))  # lists # of characters in my file path

# this shows how many characters are in the file path to my python.exe.
# my file path: ['C:\Users\Jpwig\AppData\Local\Programs\Python\Python38-32']
# subtracting length by 5, shows the number appearing directly after 'Python' showing im using version 3

print("I am using python version: %s" % python_path[len(python_path)-5])

print(sys.version_info)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
process_id = os.getpid()
print("This is using Process ID# %s" % process_id)

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print("this is my current working directory %s" % cwd)

# Print out your machine's login name
# YOUR CODE HERE
login_name = os.getlogin()
print("This is my login name: %s" % login_name)
