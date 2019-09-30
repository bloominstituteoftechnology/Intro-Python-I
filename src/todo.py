# TODO: check for item or list dups
# TODO: print out a list nicely

class TodoList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        return f"{self.name}: {self.items}"

    def __repr__(self):
        return f"TodoList({repr(self.name)})"


quit = False

all_lists = []

current_list = None

while not quit:

    command = input(f"\n(C)reate new list\n(S)elect a list ({current_list})\n(A)dd item\n(Q)uit\n\nCommand: ")

    command = command.lower().strip()  # normalize input

    if command == '':
        continue

    command = command[0]

    if command == 'q':  # quit
        quit = True

    elif command == 'c': # create
        name = input("Enter list name: ").strip()

        new_list = TodoList(name)
        all_lists.append(new_list)

        print(all_lists)

    elif command == 's': # select
        name = input("Enter list name: ").strip()

        named_list = None

        for l in all_lists:
            if l.name == name:
                named_list = l
                break  # get out of for loop

        if named_list is None:
            print(f"No such list named {name}")

        else:
            current_list = named_list

            #current_room = room[current_room].n_to  # something like this in the adv game

    elif command == 'a': # add
        if current_list is None:
            print("\n** No list selected!")

        else:
            item_name = input("Enter item: ").strip()

            current_list.items.append(item_name)