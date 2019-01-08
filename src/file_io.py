"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt', 'r') as f:
    read_data = f.read()
    print(read_data)
f.closed
# saw a "True" here in some examples but not quite sure what the function was

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# can do both of this with "r+" mode, but doing it in steps for reinforcement.
# first, open bar.txt as write-only and add the text
with open('bar.txt', 'w') as f:
    write_data = f.write('Line one \n')
    write_data2 = f.write('Line two \n')
    write_data3 = f.write('Line three')
f.closed

# now open up bar.txt as read-only to return the text
with open('bar.txt', 'r') as f:
    read_data = f.read()
    print(read_data)
f.closed