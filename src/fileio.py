# Use open to open file "foo.txt" for reading
newfile = open('foo.txt')

print('file1 ===> :')
for line in newfile:
    # Print all the lines in the file

    print(line.rstrip())
# Close the file

###############################################
newfile.seek(0)  # moving the cursor to the beginging of the file
lines = newfile.readlines()  # return an array with text
print('file2 ===>:  ', lines)

newfile.close()
###################################### file is closed


#########################################################

with open('bar.txt', 'w') as newfile2:
    newfile2.write('hello word \nhow is everything \nthank you')


with open('bar.txt', 'a') as newfile2:
    newfile2.write('\nhello hello , how is everything going thank you so much')


quote = [
    '\n helllllllllllllollllllllll',
    '\n babbabababbabbababababbabab',
    '\n iizizziziiziziziiziizizizizizi'
]

with open('bar.txt', 'a') as newfile3:
    newfile3.writelines(quote)


# Use open to open file "bar.txt" for writing

# Use the write() method to write three lines to the file

# Close the file
