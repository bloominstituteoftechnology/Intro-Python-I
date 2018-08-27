# Use open to open file "foo.txt" for reading
# f = open('foo.txt')
with open('foo.txt') as f:
# Print all the lines in the file
    for line in f:
        print line
# Close the file
# f.close()

# Use open to open file "bar.txt" for writing
# f = open('bar.txt', 'w')
with open('bar.txt', w) as f:
# Use the write() method to write three lines to the file
    f.write('But if you do, sir, I am for you. I serve as good a man as you.\n')
    f.write('No better.\n')
    f.write('Well, sir.\n')
# Close the file
# f.close()