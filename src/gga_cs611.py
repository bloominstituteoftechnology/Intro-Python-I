print(3)

# https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python#7166139

#open file
file1 = open('foo.txt', 'r')

#read file
file_contents = file1.read()

# print file
print (file_contents)



# from os import path

# #file_path = path.relpath("2091/data.txt")
# file_path = path.relpath("src/foo.txt")
# with open(file_path) as f:
# #     <do stuff>


# import os

# script_dir = os.path.dirname(__file__)
# file_path = os.path.join(script_dir, './src.txt')
# print(file_path)
# file1 = open(file_path, 'r')
# #read file
# file_contents = file1.read()

# # print file
# print (file_contents)