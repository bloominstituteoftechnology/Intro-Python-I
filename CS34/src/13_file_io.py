"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
text = "foo.txt"

with open('foo.txt', 'r') as text:
        text_list = [str(line) for line in text]
        print(text_list)

text.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar_text = "bar.txt"

with open('bar.txt', 'w') as bar_text:
        bar_text.write("hello")
        bar_text.write("this is some text")
        bar_text.write("for this file here ")
        bar_text.write("because we can")

bar_text.close()

