"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt') as f:
    print(f.read())

print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
#https://www.decodingdevops.com/python-write-to-file-line-by-line/

# YOUR CODE HERE
with open('bar.txt', 'w') as f:
    f.writelines([
        "1 + 1 = 5\n",
        "More lines to write\n",
        "What is the meaning of life?"
    ])

print(f.closed)

with open('bar.txt') as f:
    print(f.read())

print(f.closed)


"""
ANSWER:
Foo.txt
Do you bite your thumb at us, sir?
I do bite my thumb, sir.
Do you bite your thumb at us, sir?
No, sir. I do not bite my thumb at you, sir, but I bite my thumb, sir.
Do you quarrel, sir?
Quarrel, sir? No, sir.

Closed text
True

Bar.txt
1 + 1 = 5
More lines to write
What is the meaning of life?

Closed text
True

"""