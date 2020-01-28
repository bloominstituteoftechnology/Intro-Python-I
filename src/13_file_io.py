"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
file_foo= open("C:\\Users\Jason Holloway\Lambda\Intro-Python-I\src\foo.txt")
content = file_foo.read()
print(content)
file_foo.close() 

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
file_bar = open("C:\\Users\Jason Holloway\Lambda\Intro-Python-I\src\bar.txt", "a") # Use "a" to append
file_bar.write("This is line 1")
file_bar.write("This is line 2")
file_bar.write("This is line 3")
file_bar.close()
file_foo = open("C:\\Users\Jason Holloway\Lambda\Intro-Python-I\src\bar.txt", "a")
content = file_foo.read()
print(content)
file_bar.close()