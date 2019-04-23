"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
def print_file(file):
    for line in file:
        print(line)

foo = open('foo.txt', 'r')

print_file(foo)

foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open('bar.txt', 'r+')
bar.write('data1 \n')
bar.write('data2 \n')
bar.write('data3 \n')

print_file(bar)

