# Use open to open file "foo.txt" for reading
f = open('/Users/sukhada/Intro-Python/src/day-1-toy/foo.txt')
# Print all the lines in the file
text = f.read()
print(text)
# Close the file
f.close()



# Use open to open file "bar.txt" for writing
f=open('/Users/sukhada/Intro-Python/src/day-1-toy/foo.txt',"w")
# Use the write() method to write three lines to the file
f.write('Hello World\n')
f.write('Welcome to Python\n')
f.write('Closing the write function now')
# Close the file
f.close()
