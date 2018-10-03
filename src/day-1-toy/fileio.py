# Use open to open file "foo.txt" for reading
f = open("foo.txt", "r")
# Print all the lines in the file
print(f.read())
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
b = open("bar.txt", "w")
# Use the write() method to write three lines to the file
b.write("1\n")
b.write("2\n")
b.write("3\n")
# Close the file
b.close()