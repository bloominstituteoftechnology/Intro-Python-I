# Use open to open file "foo.txt" for reading
foo = open("foo.txt")

# Print all the lines in the file
for line in foo:
    print(line)

# Close the file
foo.close()


# Use open to open file "bar.txt" for writing
bar = open("bar.txt", "w")
# Use the write() method to write three lines to the file
bar.write("""Line 1
Line 2
Line 3""")
# Close the file
bar.close()