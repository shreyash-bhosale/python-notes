# 🧱 Classes & Objects in Python

## Classes = Blueprint
'''
A class is like an architect's blueprint for a house.  
The blueprint itself isn’t a house, but you can build many houses from it.  
Each house you build is called an **object**.
'''
### Example:

class Dog:
    species = "Canis lupus"   # Attribute

    def bark(self):           # Method
        print("Woof!")

# Create object
my_dog = Dog()

print(my_dog.species)  # Canis lupus
my_dog.bark()          # Woof!

class Bag:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

# Create objects
reebok = Bag("leather", 3)
campus = Bag("nylon", 2)

print(reebok.material)  # leather
print(campus.material)  # nylon
