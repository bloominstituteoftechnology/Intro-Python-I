"""
Spec: write a program that holds product and department information about a
store.  User should be able to enter a department number and get a list of
products in that department.

Product info is:
    * quantity, int
    * price
    * dept
    * name, string

You'll get product list later.

Department info:
    * number, int
    * name, string

Questions:

* How many products?

Under 1,000,000

* How to present data

Standard output

* How many customers?

Under 100 requests per second.

* Vendor accounts?

No.

* Can depts change?

No.

* Can a product be in more than one department?

Yes.

* Which depts hold what?

TBD

* How is info added?

Out of scope

* Product location?

No

* Sale info?

No
"""
class Dept:
    def __init__(self, name, num):   # Constructor
        self.name = name
        self.num = num

    def __str__(self):
        return f"Dept: {self.num}: {self.name}"

    def __repr__(self):
        return f'Dept({repr(self.name)}, {repr(self.num)})'

class Store:
    def __init__(self, name, depts):   # Constructor
        self.name = name  # "has-a" relationship
        self.depts = depts

    def __str__(self):
        s = f"Store: {self.name}\nDepartments:\n"

        for d in self.depts:
            s += f"     {d.num}: {d.name}\n"

        return s

    def __repr__(self):
        return f'Store({repr(self.name)}, {repr(self.depts)})'

    def find_dept(self, dept_num):
        for d in self.depts:
            if d.num == dept_num:
                return d

        return None


depts = [
    Dept("Department 1", 11),
    Dept("Department 2", 22),
    Dept("Department 3", 33),
]



my_store = Store("Beej's Store", depts)   # Create a new Store object
print(my_store)
print(repr(my_store))

dept_num = input("Enter a department number: ")

dept_num = int(dept_num)

dept = my_store.find_dept(dept_num)

print(dept)