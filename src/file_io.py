"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
filename = "foo.txt"
file = open(filename, "r")
for line in file:
   print (line)
file.close()
    


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain
file = open("bar.txt", "w")
lines_of_text = ["Happy Mother's Day!", "also my daughter's birthday", "my mom's is next"]
file.writelines(lines_of_text)
file.close()
