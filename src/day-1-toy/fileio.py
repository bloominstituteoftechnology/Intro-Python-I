# Use open to open file "foo.txt" for reading
file = open("foo.txt", "r")
# Print all the lines in the file
for line in file:
    print(line)
# Close the file
file.close()

# Use open to open file "bar.txt" for writing
file = open("bar.txt", "w")
# Use the write() method to write three lines to the file
first_line = "Alas, poor Yorick. \n"
second_line = "I knew him well. \n"
third_line = "To be or not to be, that is the question. \n"
file.write(first_line)
file.write(second_line)
file.write(third_line)
# Close the file
file.close()
