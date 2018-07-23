# Use open to open file "foo.txt" for reading

# Print all the lines in the file

# Close the file


# Use open to open file "bar.txt" for writing

# Use the write() method to write three lines to the file

# Close the file

f = open('foo.txt', 'r')

for line in f:
    print(line)

f.close() # garbage collector would close the file, but it is more memory efficient

g = open('foo.txt', 'w')
stuffs = ['random', 'text', 'added']
for stuff in stuffs:
    g.write(stuff + '\n')
    
g.close()