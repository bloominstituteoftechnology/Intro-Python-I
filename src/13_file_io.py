"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

foo_file = open('src/foo.txt', 'r')
print(foo_file.read())
foo_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar_file = open('src/bar.txt', 'w+')
bar_file.writelines('More\n')
bar_file.writelines('Arbitrary\n')
bar_file.writelines('Text\n')
print(bar_file.read())
bar_file.close()