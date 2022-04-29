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
print("This is the name of the program:\n", sys.argv[0])
print("Argument List:\n", str(sys.argv))
# shows: 03_modules.py

# Print out the OS platform you're using:
print("OS Platform:", sys.platform)


# Print out the version of Python you're using:
print("Python Version:", sys.version)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current Process ID:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current Working Directory:", os.getcwd())

# Print out your machine's login name
print("Machine's Name:", os.uname())

#Prints out: 
'''
This is the name of the program:
 03_modules.py
Argument List:
 ['03_modules.py']
OS Platform: linux
Python Version: 3.7.7 (default, Mar 10 2020, 17:25:08)
[GCC 5.4.0 20160609]
Current Process ID: 1550
Current Working Directory: /vagrant/github_repos/Intro-Python-I/src
    Machine's Name: posix.uname_result(sysname='Linux',
    nodename='ubuntu-xenial', 
    release='4.4.0-179-generic',
    version='#209-Ubuntu SMP
    Fri Apr 24 17:48:44 UTC 2020', machine='x86_64')
'''
