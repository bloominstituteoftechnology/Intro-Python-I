# Use open to open file "foo.txt" for reading

# Print all the lines in the file

# Close the file
filename = 'foo.txt'
file =open(filename,'r')
for line in file:
    print (line)
    file.close()


# Use open to open file "bar.txt" for writing

# Use the write() method to write three lines to the file

# Close the file
print ('Name of file: ' ,filename)
fileO = open(filename,'a')
addlines = ['first line added\n','second line added\n', 'third line added\n']
fileO.seek(0,2) 
lines = fileO.writelines( addlines )

#now print file to see dded lines
fileO.seek(0,0)
#we have a hard coded value here...need to read number of lines
for index in range(9):
    lines = fileO.next()
    print(index,lines)
fileO.close()
