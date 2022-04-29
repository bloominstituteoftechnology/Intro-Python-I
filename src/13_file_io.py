"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('foo.txt', 'r') as a_file:
    for line in a_file:
        stripped_line = line.strip()
        print(stripped_line)
a_file.close()
        
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

file1 = open(r'bar.txt','w') 
L = ["This is the first line. \n", "This is the second lind, \n", "And this is the 3rd line. \n"]
file1.writelines(L) 
file1.close()

with open('bar.txt', 'r') as b_file:
    for line in b_file:
        stripped_line = line.strip()
        print(stripped_line)
b_file.close()