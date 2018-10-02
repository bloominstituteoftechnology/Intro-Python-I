# Use open to open file "foo.txt" for reading
readFile = open('src/day-1-toy/foo.txt', 'r')
# Print all the lines in the file
print(readFile.read())
# Close the file
readFile.close()

# Use open to open file "bar.txt" for writing
writeFile = open('src/day-1-toy/bar.txt', 'w')
# Use the write() method to write three lines to the file
writeFile.write('beer\n')
writeFile.write('wine\n')
writeFile.write('shots\n')
# Close the file
writeFile.close()
