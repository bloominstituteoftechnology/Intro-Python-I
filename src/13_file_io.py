"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

with open("foo.txt") as f:
    read_data = f.read()
    print(read_data)
    f.close()
    print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

w = open("bar.txt", "w+")
w.write("line 1 \n")
w.write("line 2 \n")
w.write("line 3 \n")
w.close()

with open("bar.txt") as w:
    print(w.read())
    w.close()