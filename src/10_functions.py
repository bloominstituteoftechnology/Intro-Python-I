# # Write a function is_even that will return true if the passed-in number is even.

# # YOUR CODE HERE
def is_even(x):
    if x % 2== 0 :
        return True
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
is_even(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
def is_odd(x):
    if x %2 ==0:
        print("Even!")
    else :
        print("Odd")
# YOUR CODE HERE
is_odd(num)



def words():
    count = 0
    for i in grades:
        if i == "A":
            count = count + 3
        elif i == "B":
            count = count + 2
        elif i == "C":
            count = count + 1
        elif i == "D":
            count = count
    if count >= len(grades):
        print("Congratz!!")
    else:
        print("fail!!!")

grades = input("Enter your grades:  ")



words()

