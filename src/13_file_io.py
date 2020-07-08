"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
x = open("/Users/amin/Desktop/Lambda School/CS/Sprint_1_Python/Module_1_Python_1/Intro-Python-I/src/foo.txt", "r")
for line in x:
    print(line)
x.close()

with open("/Users/amin/Desktop/Lambda School/CS/Sprint_1_Python/Module_1_Python_1/Intro-Python-I/src/foo.txt") as x:
    read_data = x.read()
    print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
y = open('/Users/amin/Desktop/Lambda School/CS/Sprint_1_Python/Module_1_Python_1/Intro-Python-I/src/bar.txt', 'w')
y.write("Hi there")
y.write("How are you doing?")
y.write("What do you do?")
y.close()

with open("/Users/amin/Desktop/Lambda School/CS/Sprint_1_Python/Module_1_Python_1/Intro-Python-I/src/bar.txt", "w") as bar:
    bar.write("Hi there! How are you doing?")