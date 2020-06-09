"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt', 'r') as f:
    print(f.close(), f.closed)
    # // --
    # This prints all the lines and when it gets to the end enters an empty string & stops.
    # for line in f:
    #     print(line, end='')
    # \\ --

    # // --
    # This prints by line.

    # f_content = f.readline()
    # print(f_content, end='')
    # \\ --

    # // --
    # This prints 100 characters and then enters an empty string... amount of characters specified.
    # If you enter multiple times will continue where it left off and print the next 100 chracters.

    # f_content = f.read(100)
    # print(f_content, end='')
    # # f_content = f.read(100)
    # # print(f_content, end='')
    # \\ --

    # // --
    # This chunck of code sets size of content to be read to 100 chars. Then opens the content with read utilizing the
    # sized paramater. After the while loop runs sees the size read is larger than 0 so it executes the print line and then in the end
    # inserts an empty string. At that point it runes the f_content line again and re-runs size to read which is 100 lines but does not
    # execute the while loop since the content size is an empty string aka 0 so the execution ends.

    # size_to_read = 100
    # f_content = f.read(size_to_read)
    # while len(f_content) > 0:
    #     print(f_content, end='')
    #     f_content = f.read(size_to_read)
    # \\ --

    # // --
    # METHODS
    # print(f.tell())    # .tell() # Will tell the amount of characters in we are
    # print(f.seek()) -- not working   # Usually placed between prints. Will allow the print to repeat location depending on start position num placed in arg.
    # seek will also place the writing position to specified location and work like insert typing in the file.
    # .write() -- takes in content to be written into file.
    # printed -- .close() -- function to close the file
    # printed -- .closed -- checks if file has been closed.
    # printed -- .read() -- function to open file in read mode.
    # printed -- .readlines() -- function prints a list of lines contained with in the specified file
    # printed -- end=... -- variable = filevar.method('specified.file', end='') end specifies what to end with after print
    # in function scope after with open -- pass -- will allow you to skip entering. Useful for creating an empty file in write mode.
    # \\ --


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.text', 'r+') as file:
    # file.seek(0)
    # file.write("This is line one. ")
    # file.write("This is line two. ")
    # file.write("This is line three. ")
    # print(file.read())
    # print('bar.text file:', file.close(), file.closed)
    print(file.read())
