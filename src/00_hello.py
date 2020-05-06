# Print "Hello, world!" to your terminal

# print("hello, world!")

# print('hello world!')

def sum67(nums):
    summed_numbers = 0
    seven_found = False
    six_found = False
    for number in nums:
        
        if number == 6:
            summed_numbers+=0
            six_found = True
        elif number == 7:
            summed_numbers+=0
            seven_found = True
        else:
            if seven_found == True and six_found == True or seven_found == False and six_found == False:
                summed_numbers+=0
            else:
                summed_numbers+=0
        return summed_numbers
    
#    
# 
# Can you use pieces of both of the above examples to...
# Create a new list containing only the names that start with `s` so that they 
# are properly capitalized (regardless of how the name originally appears) 
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
print(names)
# TODO

s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

