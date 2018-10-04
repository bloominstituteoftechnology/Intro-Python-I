# Use open to open file "foo.txt" for reading
file = open('foo.txt')

# Print all the lines in the file
for line in file:
    print(line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file2 = open("bar.txt", "w")
# Use the write() method to write three lines to the file
file2.write("""Line 1
line2
line3""")
# Close the file
file2.close()