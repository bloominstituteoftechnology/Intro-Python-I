"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
# f = open('foo.txt', 'r')

# for line in f:
#     print(line, end="")

# f.close()

with open("/Users/lambda_school_loaner_58/Desktop/cs18/Intro-Python-I/src/foo.txt") as f:
    read_data = f.read()
    print(read_data)

    f.close()

# with open('foo.txt') as f:
#     read_data = f.read()
#     print(read_data)
# f.closed





# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f2 = open("bar.txt", "w+")

f2.write("LUKE.......SKYWALKER \n YOU'RE A WIZARD HARRY \n Aragorn..They took the little ones....")

f2.close()