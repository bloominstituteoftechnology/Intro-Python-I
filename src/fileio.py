# Use open to open file "foo.txt" for reading
object2 = open('foo.txt', 'r')

# Print all the lines in the file
# print(object)
# Close the file
str = object2.read()
print(str)

object2.close()
# Use open to open file "bar.txt" for writing
obj_bar = open("bar.txt", 'w')
# Use the write() method to write three lines to the file

obj_bar.write("Python is a great language.\nYeah its great!!\n New line")
# Close the file
obj_bar.close()
objec_read = open('bar.txt', 'r')
str2 = objec_read.read()
print(str2)
objec_read.close()