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
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f = open('bar.txt', 'w')

f.write('Movie Quotes \n')
f.write('\"Frankly, my dear, I don\'t give a damn.\" \
Gone With the Wind, 1939 \n')
f.write('\"Toto, I\'ve got a feeling we\'re not in Kansas anymore.\" \
The Wizard of Oz, 1939 \n')

f.close()
