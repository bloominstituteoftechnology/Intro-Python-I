#!/usr/bin/env python3
"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

f = open("foo.txt", 'r+')
print(f.read())
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

snippet = open("bar.txt", 'w')
snippet.write('''
* E-flat walks into a bar and the bartender said "Sorry, we dont serve minors." Ba Dum Tss
* The past, present, and future walk into a bar. It was tense.
''')
snippet.write("")
snippet.close()
