"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
import sys

def printCommandLineArguments( module ):     # creates a function to print off the methods for any module passed in as an argument
    for i in dir( module ):                  # dir(module) returns a list
        methodIndex = dir( module ).index(i) # for each index in the module's list of methods
        print(f'dir({ module }) at index of[{methodIndex}] = {i}  ')

          
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
printCommandLineArguments(sys.argv)


# Print out the OS platform you're using:
# YOUR CODE HERE
print(f'---|| line 20  OS={sys.argv[0]}')


# Print out the version of Python you're using:
# YOUR CODE HERE
print(f'---|| line 23 current version : python { sys.version}')


import os
# print(f'---|| line 2===========================0  OS={os.system()}')
os.sys
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
print(f'---|| line 27 {os}')


# Print the current process ID
# YOUR CODE HERE
print(f'---|| line 32 current process id is : {os.getpid()}')


# Print the current working directory (cwd):run
# YOUR CODE HERE
print(f'---|| line 35 print the current working directory : {os.getcwd()}')


# Print out your machine's login name
# YOUR CODE HERE
print(f'---|| line 40 My Machine\'s Login name is : {os.getlogin()}')

printCommandLineArguments(os)