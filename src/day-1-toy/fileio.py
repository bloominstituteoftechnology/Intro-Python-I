# Use open to open file "foo.txt" for reading
f = open('C:/Users/storm/LambdaSchool/Intro-Python/src/day-1-toy/foo.txt')
# Print all the lines in the file
lines = f.read()
print(lines)
# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open('C:/Users/storm/LambdaSchool/Intro-Python/src/day-1-toy/bar.txt', "w+")
# Use the write() method to write three lines to the file
f.write('This is first line\n')
f.write('This is second line\n')
f.write('This is third line')
# Close the file
f.close()