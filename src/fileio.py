# Use open to open file "foo.txt" for reading
file = open('foo.txt', 'r')

file_content = file.read()
# Print all the lines in the file
print(file_content)
# Close the file
file.close()
# Use open to open file "bar.txt" for writing
second_file = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
second_file.write("This is my first line \n")
second_file.write("This is my second line \n")
second_file.write("This is my third line \n")
second_file.close()

read_second = open('bar.txt', 'r')
second_file_content = read_second.read()
print(second_file_content)

# Close the file
read_second.close()
