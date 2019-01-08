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
# def whateves(self, parameter_list):
#     print(self)
#     print(parameter_list)

# print(whateves(sys.argv[1], sys.argv[2]))
for i in range(0, len(sys.argv)):
    print(sys.argv[i])

# Print out the OS platform you're using:
# YOUR CODE HERE
print("major: " + str(sys.getwindowsversion().major), "| platform: " + str(sys.getwindowsversion().platform), "| OS Platform: " + str(sys.platform))
# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python Version: " + str(sys.version))

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
# Print out your machine's login name
import socket
def host_name_ip():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("Hostname: ", host_name)
        print("IP: ", host_ip)
    
    except:
        print("Unable to get Hostname and IP")

print(host_name_ip())
print(os.getlogin())
# YOUR CODE HERE
