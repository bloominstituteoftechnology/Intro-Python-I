"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

foo_file = open('foo.txt')
for i in foo_file:
    print(i)
foo_file.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

stuff_to_write = '''
Hey there.
How are you?
Python is great.
'''
# # Open file for writing
# bar_file = open('bar.txt', 'w')
# # Write to file
# bar_file.write(stuff_to_write)
# # Close file
# bar_file.close()

# # Check what we wrote
# bar_file = open('bar.txt', 'r')
# for i in bar_file:
#     print(i)
# bar_file.close()


# SIMPLER
with open('bar.txt', 'w') as f:
    f.write(stuff_to_write)
with open('bar.txt', 'r') as f:
    lines = f.read()
    print(lines)
