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
# declaring the file to open and the type of action to take
print(foo.read())
 #loggin the file out in print
foo.close()
 #closing the file?....what will happen if I dont use this


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar = open('bar.txt', 'w')
bar.write('This\n')
bar.write('Guy\n')
bar.write('Codes\n')
bar.close()




file = open('hello.json', 'w')
file.write('{\n')
file.write('"greeting":"Hello!"\n')
file.write('}\n')
file.close()


read_file = open('hello.json', 'r')
print(read_file.read())
read_file.close()
