class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    # def __str__(self):
    #     return f"This student's name is {self.last_name}, {self.first_name}."

me = Student("Leo", "Sanchez")
print(me)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})."


# store

class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = f"{self.name}\n"
        for ind, category in enumerate(self.categories):
            output += " " + str(ind + 1) + ". " + category + "\n"
            
        return output

my_store = Store("The Dugout", ["Running", "BaseBall", "Basketball"])

print(my_store)

selection = input