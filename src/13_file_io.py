"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
foo = open('./src/foo.txt')
print(foo.read())
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open("src/bar.txt", "w+")
bar.write("Chicago in the Summer is beautiful\n")
bar.write("If i could live anywhere in the us it would be denver\n")
bar.write("if i could live anywhere in the world it would be Stavanger\n")
bar.close()

bar = open("src/bar.txt", "r")
print(bar.read())
bar.close()
