# Use open to open file "foo.txt" for reading
file = open("foo.txt")
# Print all the lines in the file
print(file.read())
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("bar.txt", "w")
# Use the write() method to write three lines to the file
lines = "Writing\nNew\nLines\n"
file.write(lines)
# Close the file
file.close()