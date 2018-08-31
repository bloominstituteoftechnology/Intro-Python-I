# Use open to open file "foo.txt" for reading
f = open("foo.txt")
# Print all the lines in the file
print(f.read())
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
wr = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
wr.write('This is a first line\n')
wr.write('Second line\n')
wr.write('Third Line\n')
# Close the file
wr.close()

inCaseWeActuallyWantedToSeeIt = open('bar.txt')
print(inCaseWeActuallyWantedToSeeIt.read())
inCaseWeActuallyWantedToSeeIt.close()
