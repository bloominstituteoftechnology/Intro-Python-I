# Use open to open file "foo.txt" for reading
myfile = open("foo.txt","r")
# Print all the lines in the file
for line in myfile:
   print(line)
# Close the file
myfile.close()

# Use open to open file "bar.txt" for writing
myfile = open("bar.txt","w")
# Use the write() method to write three lines to the file
myfile.write("""test
test
test""")
# Close the file

myfile.close()