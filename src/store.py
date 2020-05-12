"""
python3 store.py
The Dugout
    1. Running
    2. Baseball
    3. Basketball
    4. Exit
Select the number of a department.

Attributes:
- name
- department

Optional extra attributes:
- Store hours
- Store capacity
"""

# Composition: a "has-a" relationship
# Polymorphism: works on different data structures

from departments import Department


class Store:
    # hours = 12

    def __init__(self, name, departments):
        self.name = name
        # self.departments = departments
        self.departments = []

        for dep in departments:
            departmet = Department(dep)
            self.departments.append(departmet)

    def __str__(self):
        # return f'Store name is {self.name}'
        output = ""

        output += self.name + "\n"

        for index, department in enumerate(self.departments):
            output += str(index + 1) + ". " + str(department) + "\n"

        output += str(len(self.departments) + 1) + ". Exit"
        return output

    # __repr__ used for debugging
    def __repr__(self):
        return self


store = Store("The Dugout", ["Running", "Baseball", "Basketball", "Fencing"])
# store = Store("The Dugout", ["Running", "Baseball", "Basketball", "Fencing"])

print(store)
# print(store.hours)

selection = 0
# while selection != 4:
while selection != len(store.departments) + 1:
    selection = input("Select the number of a department. ")
    try:
        # print(type(selection))
        selection = int(selection)
        if selection >= 1 and selection < len(store.departments) + 1:
            print(f"the user selected: {selection}")
        else:
            print("Choose from the given choices")
    except ValueError:
        print("Choose a number, not an empty string or a letter or something")
    # a dynamic error message like, “please choose a number between 1 and 4”
    #​
print("Thank you for shopping with us today! :-) ")
