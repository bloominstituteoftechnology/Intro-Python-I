"""

python3 store.py
The Dugout
  1. Running
  2. Baseball
  3. Basketball
  4. Exit
Select the number of a department

Attributes:
-name
-departments

Optional Extra Attributes:
-Store hours
-Store Capacity
"""

from departments import Department

class Store:
    # hours = 12

    def __init__(self, name, departments):
        self.name = name
        self.departments = []

        for dep in departments:
            department = Department(dep)
            self.departments.append(department)

    # def __str__(self): #String is for readability
    #     return f'Store name is {self.name}'

    # def __repr__(self): #representation is for testing/debugging
    #     return f'Store name is {self.name}'

    def __str__(self):
        output = ""

        for index, department in enumerate(self.departments):
            output += str(index + 1) + ". " + str(department) +"\n"
        
        output += str(len(self.departments) + 1) + ". Exit"
        
        return output




store = Store("The Dugout", ["Running", "Basketball", "Baseball", "Fencing"])

print(store)

selection = 0

while selection != len(store.departments) + 1:
    selection = input("Select a number of a department. ")
    try:
        selection = int(selection)
        if selection >= 1 and selection < len(store.departments) + 1:
            print(f"the user selected: {selection}")
        else:
            print("Choose from the given choices")
    except ValueError:
        print(f"Choose a number")

print(f"Thank You for Shopping with Us Today :)")