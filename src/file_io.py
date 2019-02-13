"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f1 = open(r'C:\Users\Quan Nguyen\Desktop\Lambda CS\Intro-Python-I\src\foo.txt','r')
print(f1.read())
f1.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
f2 = open(r'C:\Users\Quan Nguyen\Desktop\Lambda CS\Intro-Python-I\src\bar.txt','w+')
for a in range(0,4):
    f2.write("This is abitrary "+str(a)+"\n")
f2.close()

# testing f2
f3 = open(r'C:\Users\Quan Nguyen\Desktop\Lambda CS\Intro-Python-I\src\bar.txt','r')
print(f3.read())
f3.close()