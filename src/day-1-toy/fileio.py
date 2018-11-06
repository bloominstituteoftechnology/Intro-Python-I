# Use open to open file "foo.txt" for reading
file = open('foo.txt', 'r')

# Print all the lines in the file
print(file.read())

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file2 = open('foo.txt', 'w')

# Use the write() method to write three lines to the file
file2.write( "Python is a great language.\n")
file2.write( "Javascript is a great language.\n")
file2.write( "Java is a great language.\n");

# Close the file
file2.close()
