"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open('foo.txt', 'r')
print(f.read())
# print(f.read(5))
f.close()
# print(f.read())     # --> will throw error since file was closed on previous line

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f = open('bar.txt', 'w')
# f.write('Arbitrary line 1 code')
f.write('Arbitrary line take 4\n')
f.write('Arbitrary line take 5\n')
f.write('Arbitrary line take 6\n')
f.close()
f = open('bar.txt', 'r')
print(f.read())

