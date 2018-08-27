# Use open to open file "foo.txt" for reading
f = open('foo.txt', 'r')
# Print all the lines in the file
for line in f:
    print(line, end='')
print("\n")
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open('foo.txt', "a")
# Use the write() method to write three lines to the file
f.write('If you do, sir, I am for you: I serve as good a man as you.\n')
f.write('No better.\n')
f.write('Well, sir.\n')

# Close the file
f.close()
