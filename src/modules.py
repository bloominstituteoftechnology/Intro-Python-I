import sys
import os

# Module "sys"
#
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('sys.argv==> ', sys.argv)
print('python version ==> ', sys.base_exec_prefix)
print('python version ==> ', sys.base_prefix)
print('python modules ==> ', sys.builtin_module_names)
print('python copyright ==> ', sys.copyright)
print('python copyright ==> ', sys.exec_prefix)

# Print out the plaform from sys:
print(sys.)

# Print out the Python version from sys:
print(sys.base_exec_prefix)


# Module "os"
#
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(os.getpid())

# Print the current working directory (cwd):
print(os.getcwd())

# Print your login name
print(os.getlogin())
