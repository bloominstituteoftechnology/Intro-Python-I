# Use open to open file "foo.txt" for reading
file = open("foo.txt", "r")
# Print all the lines in the file
print(file.read())
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
lines = ["line one is here\n", "line two is here\n", "line three is here\n"]
for line in lines:
    file.write(line)
# Close the file
file.close()