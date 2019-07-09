"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open("src/foo.txt", "r")
contents = f.read()
print(contents)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

a = ["reading the file or document line by line",
     "present the file in a readable format",
     "the line is short and readable" ]
# YOUR CODE HERE
f= open("src/bar.txt","w+")
for i in a:
    f.write(i+"\n")
f.close()

f = open("src/bar.txt", "r")
contents = f.read()
print("\n")
print(contents)
f.close()
