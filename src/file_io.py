"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt') as f1:
  print(f1.read())
f1.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
content = '''
  I'm bad, and that's good. 
  I will never be good, and that's not bad. 
  There's no one I'd rather be than me. 
  '''

with open('bar.txt', 'w+') as f2:
  f2.write(content)
f2.closed

with open('bar.txt') as f3:
  if f3.read() == content:
    print('Contents match')