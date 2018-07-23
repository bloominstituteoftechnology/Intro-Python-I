# Use open to open file "foo.txt" for reading
fileObj = open("foo.txt", "r")

# Print all the lines in the file
print(fileObj.read())

# Close the file
fileObj.close()

# Use open to open file "bar.txt" for writing
fileObj = open("bar.txt", "w")

# Use the write() method to write three lines to the file
fileObj.write("Hello\nWhat is\nUp")

# Close the file
fileObj.close()