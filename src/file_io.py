"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

# f = open("./foo.txt", "r")
# print(f)
# print(f.read())
# f.close()

with open('./foo.txt') as f:
    read_data = f.read()
    print(read_data)
    f.closed

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# x = open("./bar.txt", "w")

with open('./bar.txt', "w") as x:
    write_data = ["first string","second string","third string"]
    for z in write_data:
        x.write(z + "\n")
    x.closed
    
with open('./bar.txt', "r") as a:
    read_data = a.read()
    print("\n"+read_data)
    a.closed
