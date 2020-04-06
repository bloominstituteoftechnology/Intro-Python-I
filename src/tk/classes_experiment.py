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

"""Define a class that makes use of a “private” getter 
and setter for a “private” attribute.

Use the property decorator to “wire up” the getter and setter methods 
for accessing the property on an instance.

Instantiate the class and store the instance in a variable.

Test that the getter and setter methods are working when getting 
the attribute’s value and setting the attribute’s value.
"""


class Restaurant:
    def __init__(self, name, city, state):
        self._name = name
        self.city = city
        self.state = state

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


pizza_hut = Restaurant('Pizza Hut', 'Orem', 'UT')
print(pizza_hut.name)
pizza_hut.name = 'Little Caesars'
print(pizza_hut.name)
# pizza_hut.name = ''
print(pizza_hut.name)
pizza_hut.city = ''
print("Now city is: ", pizza_hut.city)

"""
Define a class that has a class method that references a class attribute when called.
Do this once using the @classmethod decorator and a second time without using the decorator.
Reflect on which method you prefer and why.
"""


class DeliveryDriver:
    count = 0

    def __init__(self, name, restaurant):
        self.name = name
        self.restaurant = restaurant
        DeliveryDriver.motto = "30 minutes or less, or it's free!"
        DeliveryDriver.count += 1

    @classmethod
    def say_motto(cls):
        print(cls.motto)

    def get_num_drivers():
        print(
            f'We currently have {DeliveryDriver.count} pizza delivery drivers!')


otto = DeliveryDriver('Otto Snowbottom', 'Pizza Hut')
hildegard = DeliveryDriver('Hildegard Kelly', 'Pizza Factory')
DeliveryDriver.say_motto()
DeliveryDriver.get_num_drivers()
