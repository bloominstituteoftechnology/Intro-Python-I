# Use open to open file "foo.txt" for reading
fa= open('foo.txt','r')
# Print all the lines in the file
for line in fa:
    print(line,end='')
# Close the file
fa.close()

# Use open to open file "bar.txt" for writing
f= open('bar.txt', 'w')
# Use the write() method to  write three lines to the file

f.write('this is line one\n')
f.write('this is line two\n')
f.write('this is line three\n')
# Close the file
f.close()