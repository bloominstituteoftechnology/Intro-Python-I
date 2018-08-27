# Use open to open file "foo.txt" for reading
file = open("foo.txt", "r") 
# Print all the lines in the file
content = file.read()
print(content)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("foo.txt", "w") 
# Use the write() method to write three lines to the file
file.write('Hello\n')
file.write('world,\n')
file.write('Python')
# Close the file
file.close()