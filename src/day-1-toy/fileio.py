# Use open to open file "foo.txt" for reading
file1 = open("src/day-1-toy/foo.txt", "r")
# Print all the lines in the file
for line in file1:
    print(line)
# Close the file
file1.close()


# Use open to open file "bar.txt" for writing
file2 = open("src/day-1-toy/bar.txt", "w")
# Use the write() method to write three lines to the file
file2.write("Hello, world!")
file2.write("This is my biography.")
file2.write("Here I come, bestseller list!")
# Close the file
file2.close()