"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open("foo.txt", "r") # f - open file named foo.txt, and 'r'ead from it
if f.mode == "r": # if the file mode is 'r', or read
    contents = f.read() #set contents (banana word) = to f.read() -- function that prints text in file
    print(contents) #print out content

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f=open("bar.txt","w+") #open file named bar.txt, w+ creates file if it does not exist
for i in range(3): # for every instance from 1-3 (3 times)
     f.write("This is line %d\r\n" % (i+1)) #write 'This is line ..'  %d is a variable for the (d)igit to be placed there, i + 1 iterates to the next step
f.close()

f = open("bar.txt", "r")
if f.mode == "r":
    contents = f.read()
    print(contents)
