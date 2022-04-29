"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open("foo.txt", "r") as foo:
    lines = foo.readlines()
    print("foo.txt:")
    for line in lines:
        print(line)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open("bar.txt", "w") as bar:
    bar.truncate(0) # Remove all text

    bar.write("This is my first line\n")
    bar.write("This is my second line\n")
    bar.write("This is my third line\n")