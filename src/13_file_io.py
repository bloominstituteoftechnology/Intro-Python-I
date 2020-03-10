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
for i in foo:
  print(i)
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

text = '''
I once knew a man from nantucket,
who wore as a hat a bucket.
his head was not strong,
he did not have long,
before the pail said fuck it
'''
# YOUR CODE HERE
bar =open('bar.txt', 'w')
bar.write(text)
bar.close()
bar = open('bar.txt','r')
for i in bar:
  print(i)
bar.close()