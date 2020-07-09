"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
import sys, os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
# Print out the command line arguments in sys.argv, one per line:
for _ in sys.argv:
    print(_)

methods = ['platform',
           'version',
           'getpid',
           'getcwd',
           'getlogin',
          ]

modules = [sys, os]

for module in modules:
    for method in methods:
        if method in dir(module):
            if hasattr(
                    getattr(module, method), '__call__'
                    ):
                print(getattr(module,method)())
            else:
                print(getattr(module, method))

