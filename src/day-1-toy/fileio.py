# Use open to open file "foo.txt" for reading
file = open("foo.txt")

# Print all the lines in the file
for line in file:
    print(line)

# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("bar.txt", "w")

# Use the write() method to write three lines to the file
file.write("""This is the first line
This is the second line
This is the third line""")

# Close the file
file.close()