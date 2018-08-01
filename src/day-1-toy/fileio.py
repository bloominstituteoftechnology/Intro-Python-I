# Use open to open file "foo.txt" for reading
f = open("foo.txt", "r")

# Print all the lines in the file
print(f.readlines())

# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open("bar.txt", "w")

# Use the write() method to write three lines to the file
f.writelines(["This is line one", "\n", "This is line two", "\n", "This is line three"])

# Close the file
f.close()
