class Product:
    def __init__(self, name, price, in_stock=
    True, on_sale=False):
        self.name = name
        self.price = price

​

def sale(self, percentage):
    return self.price * percentage

​

def return_policy(self):
    return "store credit only"

​

def __str__(self):
    return f'{self.name} costs {self.price}'

​
​

class Clothing(Product):
    def __init__(self, name, price, size, color):
        super().__init__(name, price)

​
self.size = size
self.color = color
​

def __str__(self):
    return super().__str__() + f' and has color {self.color} and size {self.size}'

​

class Swords(Product):
    def __init__(self, name, price, sharpness):
        super().__init__(name, price)
        self.sharpness = sharpness

​

def sharpen(self):
    self.sharpness += 5

​

def return_policy(self):
    return "You bleed on it, you buy it"


Collapse








