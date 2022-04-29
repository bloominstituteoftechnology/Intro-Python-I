"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE


text_file = open('foo.txt','r')
reading_text = text_file.read()
text_file.close()
print(reading_text)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# new_text = open("bar.txt", "w")

with open('bar.txt', "w") as b:
    b.write("I can code\nyou can code\nwe can code")

read_this = open("bar.txt", "r")
read_this_yes = read_this.read()
read_this.close()
print(read_this_yes)