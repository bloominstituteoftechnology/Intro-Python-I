"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

f = open('foo.txt', 'r')
f = f.read()
print(f)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

<<<<<<< HEAD
# YOUR CODE HERE

=======
>>>>>>> 445160f5a5274fb7fb007873da70e0c8dbed8d2b
my_f = open('bar.txt', 'w+')

my_f.write("Quoting Shakespeare is a little dated, don't you think? \n")

my_f.write("Let's pick out some modern snark. \n")

my_f.write("'I've worked too hard to have a clue who you are / Set the bar so far above par, we can parlay all day' - What's The Use, Mac Miller \n")

my_f.close()
