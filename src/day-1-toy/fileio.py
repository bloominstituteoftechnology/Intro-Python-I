# Use open to open file "foo.txt" for reading
file = open('foo.txt')
# Print all the lines in the file
for item in file:
    print(item)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file2 = open("bar.txt", "w")
# Use the write() method to write three lines to the file
line1 = "line1"
line2 = "line2"
line3 = "line3"
file2.writelines([line1, line2, line3])
# Close the file
file2.close
