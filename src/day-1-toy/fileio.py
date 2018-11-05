# Use open to open file "foo.txt" for reading
file = open("foo.txt", "r")
# Print all the lines in the file
print(file.read())
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
lines = ["number one, the larch, the larch\n",
         "number two, the larch, the larch\n", "number three, the larch, the larch\n"]

for line in lines:
    file.write(line)

# Close the file
file.close()
