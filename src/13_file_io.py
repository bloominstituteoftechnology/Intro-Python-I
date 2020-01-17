"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE


with open(r'C:\Users\Sarmen\PycharmProjects\HelloWorld1\Lambda_Assignments\CS Sprint 1\foo.txt') as foo:
    for item in foo:
        print(item)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

bar = open('bar.txt', 'w')

bar.write('Hello\nhello?\nHELLO!')

with open(r'C:\Users\Sarmen\PycharmProjects\HelloWorld1\Lambda_Assignments\CS Sprint 1\bar.txt') as bar:
    for item in bar:
        print(item)