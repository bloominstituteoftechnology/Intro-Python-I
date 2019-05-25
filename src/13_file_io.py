"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open('foo.txt', 'r') as fin:
    print(fin.read(), end="")
    

# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

#f = open("bar.txt", "w+")
#for i in range(10):
    #f.write("This is line %d\r\n" % (i+1))
    #f.close()



filename = 'bar.txt'
f = open(filename, 'w+')
f.write('order line 1 in bar.txt\n order line 2\n order line 3\n')
f.close()
# YOUR CODE HERE