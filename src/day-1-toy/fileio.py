# Use open to open file "foo.txt" for reading

# Print all the lines in the file

# Close the file


# Use open to open file "bar.txt" for writing

# Use the write() method to write three lines to the file

# Close the file

filename = "foo.txt"
file = open(filename)
for line in file:
    print(line)
file.close()

filename2 = "bar.txt"
file2 = open(filename2, "w")
file2.write("Hello, World. It is nice to meet you!")

