# Use open to open file "foo.txt" for reading
f=open('foo.txt')
# Print all the lines in the file
lines=f.readlines()
for line in lines:
    print('{}\n'.format(line))
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f=open('bar.txt','w')
# Use the write() method to write three lines to the file
f.write('Hey stop it.\nI said stop it.\nCut it out.\n')
# Close the file
f.close()
