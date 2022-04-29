"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
txt1 = open('src/foo.txt', 'r')
print(txt1.read())
txt1.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
txt2 = open('src/bar.txt', 'w')
txt2.write(f'\n1. Lorem Ipsum is simply dummy text of the printing and typesetting industry. \n2. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, \n3. when an unknown printer took a galley of type and scrambled it to make a type specimen book. ')

txt2.close()

txt2 = open('src/bar.txt', 'r')
print(txt2.read())
txt2.close()
