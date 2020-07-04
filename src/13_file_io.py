"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# f = open('src/foo.txt', 'r')
# print(f.readlines())
# f.close
# print(f.closed)
with open('src/foo.txt', 'r') as f:
    for line in f:
        print(line, end='')
#using the with keyword is the best practice because it will automatically close the file when it's done
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('src/bar.txt', 'w') as g:
    g.write("What did the pirate say when he walked into the bar \n")
    g.write("Ouch!!!!\n")
    g.write("maybe I need some better material")