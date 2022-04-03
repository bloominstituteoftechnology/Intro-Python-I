"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import sys
sys.path[0]

import os
with open(os.path.join(sys.path[0], "foo.txt"), "r") as f:
    print(f.read())
    f.close()


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

## This requests the new files name
# fn = input('Enter file name: ')
# try:
#     file = open(fn, 'r')
# except IOError:
#     file = open(fn, 'w')

# I tried this but it didn't work...HELP!!!/
# file_name = 'bar.txt'
# f = open(file_name, 'a+')  # open file in append mode
# f.write('python rules')
# f.close()

file = open("bar.txt", "w")
Lines = ["Is this the real life?\n", "Is this just fantasy?\n",
"Caught in a landslide\n", "No escape from reality\n"]


file = open("bar.txt", "w")
file.writelines(Lines)
file.close()

file = open("bar.txt", "r")
print(file.read())
file.close()