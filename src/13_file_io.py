"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# YOUR CODE HERE


def read_and_print(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            print(line)


read_and_print('src/foo.txt')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE


def write_lines(file_path, text_to_write):
    if isinstance(text_to_write, list) is False:
        text_to_write = text_to_write.split('\n')

    with open(file_path, 'w') as f:
        for line in text_to_write:
            f.write(f'{line}\n')


lines = [
    'To be, or not to be, that is the question:',
    "Whether 'tis nobler in the mind to suffer",
    'The slings and arrows of outrageous fortune'
]

write_lines('src/bar.txt', lines)
read_and_print('src/bar.txt')

# Uncomment the following lines to see how the write_lines function
# can handle both strings and arrays

# lines2 = "This works as well\nsince it gets converted\nto an array"
# write_lines('src/baz.txt', lines2)
# read_and_print('src/baz.txt')
