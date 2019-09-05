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
  command = input("(C)reate new list\n(S)how a list\n(A)dd item\n(Q)uit\nCommand: ")
  command = command.lower().strip()[0]

  if command == 'q':
    quit = True

  elif command == 'c':
    name = input("Enter list name: ").strip()
    new_list = TodoList(name)
    all_lists.append(new_list)

  elif command == 's'
    name = input("Enter list name: ")
    named_list = None

    for l in all_lists:
      if l.name == name:
        named_list = l
        break
      
    if named_list is None:
      print(f"There is no list called {name}")

    else:
      current_list = named_list


tl = TodoList("List #1")

#tl.items.append("Feed the alligator")
#tl.items.append("Walk (slither?) the python")
#print(tl)
