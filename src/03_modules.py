"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# Import modules we will use:
import getpass
import os
import sys


# --------------------------------------------------------------------------------
# PART 1: SYS MODULE

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print("\nArguments entered:")
for num, arg in enumerate(sys.argv):
    print(f"Argument #{num}: {arg}")

# Print out the OS platform you're using:
current_platform = sys.platform
print(f"\nUsing platform: {current_platform}" + (" (macOS)" if current_platform == "darwin" else ""))

# Print out the version of Python you're using:
print(f"Using Python version: {sys.version}\n")


# --------------------------------------------------------------------------------
# PART 2: OS MODULE

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f"Current process ID: {os.getpid()}")

# Print the current working directory (cwd):
print(f"Current working directory: {os.getcwd()}")

# Print out your machine's login name
print(f"Login name: {os.getlogin()}")
print(f"Portable version (not only local): Current login name: {getpass.getuser()}\n")
