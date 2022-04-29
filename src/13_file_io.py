"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""


# Import libraries and modules we will use:
import os
import sys


# --------------------------------------------------------------------------------
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# Check to make sure we're in the right directory before trying to open the file:
try:
    assert os.getcwd()[-3:] == "src"
except AssertionError as assert_error:
    print(f"Error: Please make sure you are in the right directory for this file.\n")
    sys.exit()

# Read and print the contents of 'foo.txt':
try:
    with open("foo.txt") as file:
        contents = file.read()
except FileNotFoundError as file_error:
    print(f"Error: The file {str(file_error).split(': ')[-1]} does not exist in this directory.\n")
    sys.exit()

print(f"""\nContents of file 'foo.txt': \n"{contents}"\n""")


# --------------------------------------------------------------------------------
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# Write content into new file 'bar.txt':
with open("bar.txt", 'w') as new_file:
    new_file.write("[three lines of arbitrary content]\n")
    new_file.write(contents)

# Read and print all content from our newly created file, 'bar.txt':
try:
    with open("bar.txt", "r") as new_file:
        print(f"Contents of file 'bar.txt': \n{new_file.read()}\n")
except FileNotFoundError as file_error:
    print(f"Error: The file {str(file_error).split(': ')[-1]} does not exist in this directory.\n")
    sys.exit()
