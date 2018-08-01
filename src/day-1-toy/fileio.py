# Use open to open file "foo.txt" for reading
f= open("foo.txt","r")

# Print all the lines in the file

contents = f.read()
print(contents)
     
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
g= open("bar.txt","w+")

# Use the write() method to write three lines to the file
g.write('Hello line 1\n')
g.write('How are you?\n')
g.write('What s hot day!')

# Close the file
g.close()