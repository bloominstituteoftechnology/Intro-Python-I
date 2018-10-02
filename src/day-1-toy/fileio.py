# Use open to open file "foo.txt" for reading
file_object = open("foo.txt")
# Print all the lines in the file
print(file_object.read())
# Close the file
file_object.close()

# Use open to open file "bar.txt" for writing
file_object = open("bar.txt", "w")
# Use the write() method to write three lines to the file
file_object.write("Old pond")
file_object.write("Frog leaping")
file_object.write("Splash")
# Close the file
file_object.close()