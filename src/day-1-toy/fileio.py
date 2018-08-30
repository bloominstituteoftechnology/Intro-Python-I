# Use open to open file "foo.txt" for reading
f = open("foo.txt")
# Print all the lines in the file
print(f.read())

# Close the file
f.close()

# Use open to open file "bar.txt" for writing
b = open("bar.txt")

# Use the write() method to write three lines to the file
b.write("I love Lambda\n I love Python\n Lets Go!\n")

# Close the file
b.close()
