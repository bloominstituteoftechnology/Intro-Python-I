"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
foo = open('foo.txt', 'r')
data = foo.read()
print(data)
foo.close()
print(foo.closed)
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open('bar.txt', 'w')
line1 = "This is some arbitrary stuff\n"
line2 = "We like to party, we like... we like to party\n"
line3 = "Merp Merp\n"
writeList = [line1, line2, line3]
for line in writeList:
    bar.write(line)
bar.close()
bar = open('bar.txt', 'r')
my_journal = bar.read()
print(my_journal)
bar.close()