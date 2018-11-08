# Use open to open file "foo.txt" for reading
i = open("foo.txt")

# Print all the lines in the file
for line in i:
    print(line)

# Close the file
i.close()


# Use open to open file "bar.txt" for writing
b = open("bar.txt", "w")

# Use the write() method to write three lines to the file
b.write("Hello, how is it \n")
b.write("Hello, My name is Jeff \n")
b.write("Hey, My name is Huthman \n")

# Close the file
b.close()