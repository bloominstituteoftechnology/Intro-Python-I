# Use open to open file "foo.txt" for reading
f = open('/Users/cave-computer/Documents/LambdaSchool/cs/python/Intro-Python/src/day-1-toy/foo.txt', 'r')
# Print all the lines in the file
for line in f:
    print(line)

# Close the file
f.close()

# Use open to open file "bar.txt" for writing
f = open('/Users/cave-computer/Documents/LambdaSchool/cs/python/Intro-Python/src/day-1-toy/bar.txt', 'w')

# Use the write() method to write three lines to the file
for number in range(3):
    f.write(number)
# Close the file
f.close()