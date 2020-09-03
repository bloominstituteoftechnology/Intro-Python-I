"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open("foo.txt") as f:
    for line in f:
        print(line)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bukowski = open("bar.txt", "w")

line1 = "You begin saving the world by saving one man at a time; \n"
line2 = "all else is grandiose romanticism\n"
line3 = "or politics.\n"
bukowski.writelines([line1, line2, line3])
bukowski.close()
# print(bukowski.read())

# YOUR CODE HERE