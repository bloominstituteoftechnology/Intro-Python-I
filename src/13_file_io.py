"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
reading = open("foo.txt", "r")
print(reading.read())
reading.close()



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
writing = open("bar.txt", "w")
writing.write("Hi there")
writing.write("\nI am here")
writing.write("\nNow I am gone")
writing.close()

readly = open("bar.txt", "r")
print(readly.read())
readly.close()