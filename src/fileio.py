# Use open to open file "foo.txt" for reading
userFile = open('foo.txt', 'r')
# Print all the lines in the file
print(userFile.read())
# Close the file

userFile.close()
# Use open to open file "bar.txt" for writing
userFile2 = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
userFile2.write(
    'Ride with the mob\nAlhamdulallah\nCheck in with me, and do ya job')
# Close the file
userFile2.close()
