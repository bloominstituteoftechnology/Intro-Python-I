"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import platform
import os
import getpass

print('Argument Len', len(sys.argv))

print('OS Platfrom I am using:', platform.platform())

print('version of Python I am using:',sys.version)

print('Get current PID:',os.getpgid(1))

print('Get current working directory:', os.getcwd())

print('Machine Login name:', getpass.getuser())
