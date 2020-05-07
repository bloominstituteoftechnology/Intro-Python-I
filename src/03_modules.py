"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
import os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
import sys
# Brought this in as stretch to get last problem working in WSL2!!!
import pwd


# Print out the command line arguments in sys.argv, one per line:
print('> sys.argv contains:')
for each in sys.argv:
    print('    ' + each)

# Print out the OS platform you're using:
print('> OS: ' + sys.platform)

# Print out the version of Python you're using:
print('> Python v' + sys.version)


# Print the current process ID
print('> PID: ' + str(os.getpid()))
print('> PPID: ' + str(os.getppid()))


# Print the current working directory (cwd):
print('> Current Directory: ' + os.getcwd())

# Print out your machine's login name

# The below SHOULD work but it doesn't in WSL2 since there is no effective active user
# print('> Login: ' + os.getlogin())

# Workaround for WSL2 to get the same answer as the above would get!
print('> Login: ' + pwd.getpwuid(os.getuid()).pw_name)
