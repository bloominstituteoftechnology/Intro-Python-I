# Use open to open file "foo.txt" for reading
file = open('foo.txt', "r")
# Print all the lines in the file
for line in file:
    print(line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file1 = open("bar.text","w")

# Use the write() method to write three lines to the file
# file1.write('First line,\n')
# file1.write('Second line,\n')
# file1.write('Third line')
# ********** v2
# file1.write("Line1\nLine2\nLine3\n")
# ********** v3
file1.write("""Line 1
Line 2
Line 3""")

# Close the file
file1.close()