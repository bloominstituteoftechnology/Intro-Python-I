"""Challenge 1
1. Define a class
2. Instantiate the class twice, storing each instance in a separate variable.
3. Print out the two class instances and make sure they are showing the class 
that you created and two distinct locations in memory.
"""


class Pizza:
    def __init__(self, name, toppings, category):
        self.name = name
        self.toppings = toppings
        self.category = category

    def about(self):
        return f'The {self.name} is a {self.category} pizza with {len(self.toppings) + 1} toppings.'


kiddie = Pizza('Kiddie', ['cheese'], 'basic')
print(kiddie)
print(kiddie.about())

veggie = Pizza('Veggie Lovers', ['artichokes', 'mushrooms', 'black olives', 'green olives',
                                 'green peppers', 'spinach', 'basil', 'fresh tomatoes', 'corn', 'zucchini'], 'gourmet')
print(veggie)
print(veggie.about())


"""Challenge 2

1. Define a class
2. In the class definition, define the __init__, __str__, and __repr__.
3. Instantiate the class and store the instance in a variable.
4. Interact with the variable to test that the __str__ and __repr__ methods are working as you’d expect based on your definition.
"""


class Customer:
    def __init__(self, name, eater_type, article, appetite_size):
        self.name = name
        self.eater_type = eater_type
        self.article = article
        self.appetite_size = appetite_size

    def __str__(self):
        return f'{self.name} is {self.article} {self.eater_type} and has a {self.appetite_size} appetite.'

    def __repr__(self):
        return f'Customer({self.name}, {self.eater_type}, {self.article}, {self.appetite_size})'


me = Customer('Heather', 'vegetarian', 'a', 'medium')
print(me)
