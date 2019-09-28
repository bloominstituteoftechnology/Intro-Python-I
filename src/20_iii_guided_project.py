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

    def __init__(self, name, num): #constructor
        self.name = name
        self.num = num

    def __str__(self):
        return f"Dept: {self.num}: {self.name}"

    def __repr__(self):
        return f'Dept({repr(self.name)}, {repr(self.num)})'


class Store:

    def __init__(self, name, depts): #constructor
        self.name = name #'has-a' relationship
        #self.in_business = True
        self.depts = depts #'has-a' relationship
        #print("~~~~~Constructor was called!!~~~~~")
        #print(self)

    def __str__(self):
        s = f"Store: {self.name}\nDepartments:\n"

        for d in self.depts:
            s += f"     {d.num}: {d.name}\n"

        return s

    def __repr__(self):
        #return f'Store("' + self.name + '")' #alt solution
        return f'Store({repr(self.name)}, {repr(self.depts)})'

    def find_dept(self, dept_num):
        for d in self.depts:
            if d.num == dept_num:
                return d
        return None


depts = [
  Dept("Ladies Clothing", 1),
  Dept("Ladies Shoes", 2),
  Dept("Juniors Clothing", 7)
]

#print("I am before the constructor call")
my_store = Store("Rainy Day Resale", depts)
print(my_store)
#print(repr(my_store))
#print("I am after the constructor call")

#my_store.name = "Downtown Barber"
#print(repr(my_store))

dept_num = input("Ender a department number: ")
dept_num = int(dept_num)

dept = my_store.find_dept(dept_num)

print(dept)

#dept1 = Dept("Department 1")
#print(dept1)
#print(repr(dept1))