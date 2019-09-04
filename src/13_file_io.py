"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f= open("foo.txt", "r")
for e in f:
    print(e)
f.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
k=open("bar.txt" ,"a")
k.writelines("There are more things to be written.\nWhat can I add to this. \n I want to write more on this.")
k.close()
p= open("bar.txt","r")
for e in p:
    print(e)
