"""
Import Statements:
"""

from Notebooks import LatLon

# Design a store using OOP methodologies


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} costs ${self.price}"


class Department:
    # products with a list of tuples with signature (string, int)
    def __init__(self, name, products=[]):
        self.name = name
        self.products = [Product(*p) for p in products]

    def __str__(self):
        return f"No products available in the {self.name} department yet."

# what does this store look like?
# what are attributes we care about?
# a name
# location
# categories of products
# a store needs product


class Store:
    def __init__(self, name, lat, lon, departments):
        self.name = name
        self.location = LatLon(lat, lon)
        self.departments = [Department(d) for d in departments]

    # add a __str__ method so that can observe our Store instance
    def __str__(self):
        return f"Store {self.name}, {self.location}, {self.departments}"


store = Store("LambdaStore", 44.13455, -121.123124,
              ["Clothing", "Cookware", "Books", "Sporting Goods"])
# print(store)

# we want to add departments
# let's take input from the user and have them specify departments by the department's
# index in the departments list

# wrap all this logic in a while loop so that we can keep giving selections
# instead of having re-run the program every time
while True:
    selection = input("Select the number of a department or type 'exit' to leave: ")

    if selection == "exit":
        print("Thanks for shopping with us!")
        break

    # add error handling so that when a user inputs a department for a non-existent
    # department, we'll notify them that that department doesn't exist
    try:
        # casting might cause an error
        selection = int(selection)
        if selection >= len(store.departments):
            print("That's not a valid department")
        elif selection >= 0 and selection < len(store.departments):
            print(f"{store.departments[selection]}")
        else:
            print("Department numbers are positive")
    except ValueError:
        # the user didn't give us a value that could be cast to a number
        print("Please enter your choice as a number")

    # when should we break out of this loop?
    # let's let the user type "exit" into the selection to have them leave
