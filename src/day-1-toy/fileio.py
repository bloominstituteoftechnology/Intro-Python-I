# Use open to open file "foo.txt" for reading
traceOn = open("foo.txt")

# Print all the lines in the file
for line in traceOn:
    print(line)

# Close the file
traceOn.close()

# Use open to open file "bar.txt" for writing
traceOn = open("bar.txt", "w")

# Use the write() method to write three lines to the file
traceOn.write("""Line One
Line Two
Line Three""")

# Close the file
traceOn.close()
