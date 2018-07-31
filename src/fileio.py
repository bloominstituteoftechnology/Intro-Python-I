# Use open to open file "foo.txt" for reading

file = open('foo.txt', 'r')

# Print all the lines in the file
for line in file:
  print(line)
# Close the file

file.close()


# Use open to open file "bar.txt" for writing

file = open('bar.txt', 'w')

# Use the write() method to write three lines to the file
file.write('Do you bite your thumb at us, sir?\n')
file.write('I do bite my thumb, sir.\n')
file.write('Do you bite your thumb at us, sir?\n')

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

file.close()

# Close the file