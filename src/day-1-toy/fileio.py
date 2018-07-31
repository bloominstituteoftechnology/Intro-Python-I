# Use open to open file "foo.txt" for reading
import os
foo = open('foo.txt')
# Print all the lines in the file
for lines in foo:
  print(lines)
# Close the file

foo.close()


# Use open to open file "bar.txt" for writing
# creates a file if it doesn't exist
# Use the write() method to write three lines to the file





# Close the file
# def write_new_file():
#   name = input('Name your file: ')
#   file = open('{}.txt'.format(name), 'w+' or 'r')
#   print('file named "{}" created '.format(name))
#   num = input('How many lines do you want to create? ')
#   for i in range(int(num)):
#     string = input('Type your new line here: ')
#     file.write('{} \n'.format(string))
#   file.close()
#   print('File named "{}" is now closed'.format(name))


def write_new_file():
  print("Let's make a new file! \n")
  name = input("Name your new file, don't forget the file type: ")
  file = open(name, 'w+' or 'r')
  print('file named "{}" created!'.format(name))
  num = input('How many lines do you want to write? ')
  for i in range(int(num)):
    line = input('Write a line: ')
    file.write(str(line) + '\n')
    print('line written!')
  file.close()
  print('file named "{}" closed'.format(name))

write_new_file()