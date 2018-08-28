# Use open to open file "foo.txt" for reading
f = open('foo.txt')
# Print all the lines in the file
print(*f)
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
bar = open('bar.txt', 'w')
# Use the write() method to write three lines to the file
bar.write('I know that is is all over\nBut I want to keep going\nI am getting sleepy now')
print(*bar)
# Close the file
bar.close()

#ask why I was getting issues on this on run, though file was created