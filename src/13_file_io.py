"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
with open('foo.txt') as f:
    for line in f:
        print(line, end='')
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

b =  open('bar.txt', 'w')

val = ('This is one line.\nThis is second line.\nThis is the third line')

txt = str(val)
b.write(txt)
b.close()

