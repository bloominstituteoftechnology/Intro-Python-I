# Use open to open file "foo.txt" for reading
# Print all the lines in the file
# Close the file
with open("foo.txt") as x:
    read_lines = x.read()
    print(read_lines)
x.closed

# Use open to open file "bar.txt" for writing
# Use the write() method to write three lines to the file
# Close the file
with open("bar.txt", "w+") as y:
    write_lines = y.write("Python\nIs\nNeat\n")
y.closed
