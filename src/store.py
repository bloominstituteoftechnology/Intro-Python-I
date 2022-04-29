"""
python3 store.py 

The Dugout
    1.Runnign 
    2 Baseball
    3.Basketball
    4.Exit

    Select the number of departments
Attributes 
 - name
 - departments 


"""


class Store:
    #hours = 12 
    def __init__(self, name, department):
        self.name = name
        self.department = department


    def __str__(self):
        output = ""

        output += self.name + "\n"

        for index, department in enumerate(self.departments):
            output += str(index + 1) + ". " department




store  = Store("The Dugout", ["Running", "Baseball", "Basketball"])

print(store)

