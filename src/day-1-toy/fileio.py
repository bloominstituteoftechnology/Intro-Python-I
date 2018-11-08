# Use open to open file "foo.txt" for reading
myfile = open("./foo.txt")
# Print all the lines in the file
myfile.seek(0)
print(myfile.readlines())
# Close the file
myfile.close()

# Use open to open file "bar.txt" for writing
with open("bar.txt", mode="w+") as new_file:
# Use the write() method to write three lines to the file
    new_file.write("first line" "\nsecond line" "\nthird line")
with open("bar.txt", mode="r") as new_file:
    print(new_file.readlines())
# Close the file
new_file.close()