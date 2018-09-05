# Use open to open file "foo.txt" for reading
fp = open("foo.txt")

# Print all the lines in the file
for i in fp:
    print(i)

# Close the file
fp.close()

# Use open to open file "bar.txt" for writing
fp = open("bar.txt", "w")

# Use the write() method to write three lines to the file
fp.write("""Line,
Line,
Line""")

# Close the file
fp.close()