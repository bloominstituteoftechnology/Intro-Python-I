# Use open to open file "foo.txt" for reading
filename = "foo.txt"
file = open(filename, "r")

# Print all the lines in the file
for line in file:
    print(line)

# Close the file
file.close()


# Use open to open file "bar.txt" for writing
fh = open("bar.txt", "w")

# Use the write() method to write three lines to the file
lines_of_text = ["a line of text\n", "another line of text\n", "a third line\n"]
fh.writelines(lines_of_text)

# Close the file
fh.close()
