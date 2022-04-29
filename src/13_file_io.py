"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

foo = open('foo.txt', 'r')
foo_contents = foo.read()
print(foo_contents)  # Complete!

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open('bar.txt', 'w')
bar_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus interdum vel lorem id commodo. Morbi dictum in sem ut sodales.
Donec venenatis porttitor tellus sit amet consectetur.'''
bar.write(bar_text)
bar.close()  # Complete!

# Checking contents now as instructions state.
bar = open('bar.txt', 'r')
bar_contents = bar.read()
print(bar_contents)  # Complete!
