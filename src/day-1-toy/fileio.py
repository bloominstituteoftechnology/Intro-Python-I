# Use open to open file "foo.txt" for reading
f = open("foo.txt")

# Print all the lines in the file
for line in f:
    print(line)

# Close the file
f.close()


# Use open to open file "bar.txt" for writing
b = open("bar.txt", "w")

# Use the write() method to write three lines to the file
b.write("""A new Line
Another Line
Too Many Lines""")

# Close the file
b.close()