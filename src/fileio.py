# Use open to open file "foo.txt" for reading
file = open("foo.txt")

# Print all the lines in the file
print(file.read())

# Close the file
file.close()


# Use open to open file "bar.txt" for writing
f = open("bar.txt")

# Use the write() method to write three lines to the file
# f.write("Hello")
# f.write("World")
# f.write("It's me, Beyonce")

print(f.read())

# Close the file

f.close()