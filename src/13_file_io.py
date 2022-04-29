"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open(r'src\foo.txt')

for line in f:
    print(line)

f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f2 = open(r'src\bar.txt', 'w')
f2.write('one ')
f2.write('two ')
f2.write('three ')
f2.close()


f2 = open(r'src\bar.txt')

for line in f2:
    print(line)

f2.close()
