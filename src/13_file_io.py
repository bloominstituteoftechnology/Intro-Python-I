"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

files = open('C:\\Python\\Intro-Python-I\\src\\foo.txt')
print(files.read())
files.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

fileTwo = open('C:\\Python\\Intro-Python-I\\src\\bar.txt', 'w+')
fileTwo.write('I love Python.\nBut I cant forget JS\nBoth are very good programming languages')
fileTwo.close()
fileTwo = open('C:\\Python\\Intro-Python-I\\src\\bar.txt')
print(fileTwo.read())
fileTwo.close()


