class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(f"Welcome to {self.name}! Which deparment would you like to use it?")

        for d in self.departments:
            print(d)

# Should department inherit from Store?
class Department:
    def __init__(self, name, products, id):
        self.id = id
        self.name = name
        self.products = products
        

    def __str__(self):
        return f"{self.id}: {self.name}"

store = Store("The Dugout", [
    Department(1, "Baseball", []),
    Department(2, "Basketball", []),
    Department(3, "Football", []),
    Department(4, "Golf", []),
])
# Loop forever while the user is browsing through departments:
# Use the "input" function to prompt the user to select a department to browse

while True:
    # Print a welcome message for the store. 
    store.print_welcome()

    #get the apartment number the user wants to visit:
    selection = input("What department would you like to visit? ")

    # If the user types "Quit", exit the program
    if selection == "quit":
        break

    chosen_department = store.departments[int(selection) - 1]

    print("You picked the {chosen_department.name} department.\n")
