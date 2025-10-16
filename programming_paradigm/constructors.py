'''class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Create a Point object
point = Point(3, 5)
print(f"Point coordinates: ({point.x}, {point.y})")  # Output: Point coordinates: (3, 5) '''

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age:{self.age}"
person = Person("Alice", 30)
print (person)'''


import csv 

class Item:
    all = []
    def __init__(self, name:str, price: float, quantity = 0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
    def calculate_total_price(self):
        return(self.price * self.quantity)
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            Item = list(reader) 

        for item in item:
            print(item) 
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
Item.instantiate_from_csv()

"""print(f"Total Price for {Item1.name}: {Item1.calculate_total_price()}")
print(f"Total Price for {Item2.name}: {Item2.calculate_total_price()}")
print(f"Total Price for {Item3.name}: {Item3.calculate_total_price()}")
print(f"Total Price for {Item4.name}: {Item4.calcula    te_total_price()}")
print(f"Total Price for {Item5.name}: {Item5.calculate_total_price()}")
print(f"Total Price for {Item6.name}: {Item6.calculate_total_price()}")"""


print(Item.all)