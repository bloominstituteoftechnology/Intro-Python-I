# # x = 2

# # def multiply(x):
# #     return x * 2

# # print(multiply(x))

# # #------------------------------
# # l= [1,2,3,4,5]

# # def multiply_list(l):
# #     for i in range(len(l)):
# #         l[i] *=2
# #     return l
# # print(multiply_list(l))

# # y = multiply(12)
# # print(y)

# import random
# # Create a rock/paper/scissors REPL loop
# # Have a computer AI to play against us
# # Keep track of the score
# # Rules: r beats s, s beats p, p beats r
# ​
# wins = 0
# losses = 0
# ties = 0
# choices = ['r', 'p', 's']
# ​
# while True:
#     print(f"Score: {wins} - {losses} - {ties}")
#     cmd = input("\nChoose r/p/s: ")
#     # AI picks a random choice from r/p/s
#     ai_choice = choices[random.randrange(3)]
#     print (f"Computer chose {ai_choice}")
#     if cmd == "r":
#         if ai_choice == 'p':
#             losses += 1
#             print("You lose")
#         elif ai_choice == 's':
#             wins += 1
#             print("You win!")
#         elif ai_choice == 'r':
#             ties += 1
#             print("You tie.")
#     elif cmd == "p":
#         if ai_choice == 's':
#             losses += 1
#             print("You lose")
#         elif ai_choice == 'r':
#             wins += 1
#             print("You win!")
#         elif ai_choice == 'p':
#             ties += 1
#             print("You tie.")
#     elif cmd == "s":
#         if ai_choice == 'r':
#             losses += 1
#             print("You lose")
#         elif ai_choice == 'p':
#             wins += 1
#             print("You win!")
#         elif ai_choice == 's':
#             ties += 1
#             print("You tie.")
#     elif cmd == "q":
#         print("Goodbye!")
#         break
#     else:
#         print("I do not understand that command.")

# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print(tel)
# del tel['jack']
# print(tel)

# def loop_50_times(array):
#     for i in range(40):
#         print(i)

# def print_pairs(items):
#     for item_one in items:
#         for item_two in items:
#             print('Print',item_one, item_two)

# def do_a_bunch_of_stuff(items):
#     last_idx = len(items) - 1
#     print(items[last_idx])

# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay

#     def fullname(self):
#         return '{} {} {}'.format(self.first, self.last, self.pay)

# emp1 =Employee('Hamid', 'Azizy', 5000)
# emp2 = Employee('Amin', 'Azizy', 4000)

# print(emp1.first)
# print(emp2.first)
# print(emp1.fullname())

# class Animal:
#     def __init__(name, hunger, diet):
#         self.name = name
#         self.hunger = hunger
#         self.diet = diet

#     def eat(self, food):
#         if food>0 and hunger<25:
#             hunger += food

