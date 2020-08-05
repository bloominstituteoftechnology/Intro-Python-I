"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
# ____ Reading
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
# input file
foo = "foo.txt"
outputfile = "bar.txt"

with open(foo) as f1:
    for line in f1:
        print(line)

# -------------> Writing
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open(outputfile, 'a') as f2:
    f2.write('''
                This is line one
                This is line two
                This is line ....... three
                ''')
