"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

text = open('foo.txt')
print(text.read())
text.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain
print('\n\n')
    
new_file = open('bar.txt', 'w')
new_file.write("I went to have an interview as a carpenter today")
new_file.write("\nOh really? Well, good luck!")
new_file.write("\nYeah, I think I really nailed it!")
new_file.close()
text = open('bar.txt')
print(text.read())
text.close()


# YOUR CODE HERE