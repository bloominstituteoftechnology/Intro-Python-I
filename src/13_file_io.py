"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# lets do this os agnostic
# first I get the absolute path of this file. Since foo.txt is located in the
# same directory, I then get the directory name.  Then I join the directory 
# with the file name to get an OS agnostic absolute path
import os

filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'foo.txt')

with open(filepath, 'r') as f:
    data = f.read()
    print(data)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bar.txt')

# triple quotes preserve newlines, so no need to use /n
three_lines = '''If you do, sir, I am for you: I serve as good a man as you.
No better.
Well, sir.'''

with open(filepath, 'w+') as writefile:
    writefile.write(three_lines)
writefile.close()

with open(filepath, 'r') as readfile:
    print(readfile.read())
readfile.close