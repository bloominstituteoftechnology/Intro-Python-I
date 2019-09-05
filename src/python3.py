class TodoList:
    def __init__(self, name):
        self.name = name
        self.items = []
    def __str__(self):
        return f"{self.name}: {self.items}"
    def __repr__(self):
        #Representation of our list (for developers) -- prints out a representation in console of what you are trying to obtain
        return f"TodoList({repr(self.name)})"

quit = False
all_lists = []
current_list = None

while not quit:

    command = input("(C)reate new list\n(S)elect a list ({current_list})\n(A)dd item\n(Q)uit\nCommand: ")

    command = command.lower().strip() # strip allows white space before and after input and strips it away. 
   

    if command == '':  # if they enter nothing
        continue  # continue starts the loop or function over
    command = command[0] #[0] is for grabbing first letter in case they type Quit

    if command == 'q':
        quit = True
    elif command == 'c':
        name = input('Enter list name: ').strip()
        new_list = TodoList(name)
        all_lists.append(new_list)
        print(all_lists)
    elif command == 's':
        name = input('Enter list name: ').strip()

        named_list = None
        for l in all_lists:
            if l.name == name:
                named_list = l
                break

        if named_list is None:
            print(f">>> No such list named {name}")
        else:
            current_list = named_list # this makes a reference to the list, NOT a copy
            print(f">>> {current_list}")
    elif command == 'a':
        item_name



# tl = TodoList("list 1")
# tl.items.append("Get Milk")
# tl.items.append("Go to store")
# print(tl)