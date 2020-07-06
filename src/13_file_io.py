"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open("foo.txt", "r") as f:
    print("foo.txt:")
    for line in f:
        # Remove newlines and indentation from lines
        text = line.strip()
        # Indent each line in the file
        print(f"    {text}")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open("bar.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("Nice day, isn't it?\n")
    f.write("Enjoy the weather :3\n")
