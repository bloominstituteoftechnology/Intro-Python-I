# Use open to open file "foo.txt" for reading
file = open("foo.txt", "r")
file_contents = file.read()
# Print all the lines in the file
print(file_contents)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("bar.txt", "w")
# Use the write() method to write three lines to the file
file.write("Amazing \nLet's Go \nSteelers!!!")
# Close the file
file.close()