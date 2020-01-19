"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:

import sys
import os

for x in sys.argv:
    print('Argument:', x)
    
print('Program Name', sys.argv[0])
print('Arguments', sys.argv[1:])
print('Count of Arguments', len(sys.argv))

# Print out the OS platform you're using:
platform = sys.platform
switcher = {
    
}

# Print out the version of Python you're using:
print('The Python version I am using on my {0} machine is {1}.format(switcher.get(platform, 'Invalid OS'), sys.version))


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f' The current process id is (os.getpid())')

# Print the current working directory (cwd):
os.chdir('C:/Users/Owner/Desktop/Lambda School Projects/Intro-Python-I/src')
print(f'The current directory is (os.getcwdb())')

# Print out your machine's login name
print('The current user is', os.getlogin())
