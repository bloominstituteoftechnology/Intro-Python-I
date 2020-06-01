"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os
print(os.getcwd())

def print_file(fileName):
    with open(fileName, 'r') as file:
        data = file.read()
        print(data)

print_file('foo.txt')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open('bar.txt', 'w') as newFile:
    newFile.write('Ice, ice, icicles\n')
    newFile.write('Pop, pop, popcicles\n')
    newFile.write('Test, test, testing 1...2...3...\n')

print_file('bar.txt')