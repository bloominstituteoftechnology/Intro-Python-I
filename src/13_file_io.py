"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
def foo():
    with open('foo.txt') as f:
        info = f.read()
        print(info)
# We can check that the file has been automatically closed.
    print(f.closed)

print(foo())
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

def bar():
    text_file = open("bar.txt", "w")
    text_file.write("Happy\n")
    text_file.write("Birthday\n")
    text_file.write("Stephanie")
    text_file.close()

    with open('bar.txt') as f:
        info = f.read()
        print(info)
        
    print(f.closed)
print(bar())