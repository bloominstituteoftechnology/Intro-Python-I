# Use open to open file "foo.txt" for reading
f = open('src/day-1-toy/foo.txt', 'r')
# Print all the lines in the file
foo_text = f.read()
print(foo_text)
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
b = open('src/day-1-toy/bar.txt', 'w')
# Use the write() method to write three lines to the bfile
b.write('Cash rules everything around me\n') 
b.write('CREAM Get the money\n')
b.write('Dolla dolla bills, yall\n')
# Close the file
b.close() 