"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
# f = open('foo.txt', 'r')
# print(f.read())
# f.close()

with open('foo.txt', 'r') as f:
    read_data = f.read()
f.close
print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

# bar = open('bar.txt', 'w')
# L = ["str1", "str2", "str3"]
# # bar.write("1234")
# bar.writelines(L)
# bar.close
# test = open("bar.txt", "r")
# print(test.readlines())
# test.close()

with open('bar.txt', 'w') as t:
    t.write("asd")
t.close
