# Use open to open file "foo.txt" for reading
with open("./src/day-1-toy/foo.txt") as file_object:
    contents = file_object.read()
    print(contents.strip())

# Print all the lines in the file

# Close the file


# Use open to open file "bar.txt" for writing
with open("./src/day-1-toy/bar.txt", "w") as file_object:
    file_object.write("Hello\n")
    file_object.write("Hello\n")
    file_object.write("Hello\n")

# Use the write() method to write three lines to the file

# Close the file
