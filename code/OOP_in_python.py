
# =========================================
# OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
# =========================================

# Three Ways to Write the Same Logic

# 1. Imperative Approach (basic, not reusable)
a, b = 5, 3
print("Imperative Result:", a + b)

# 2. Functional Approach (reusable using functions)
def add(a, b):
    return a + b

print("Functional Result:", add(5, 3))

# 3. Object-Oriented Approach (structured & scalable)
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print("OOP Result:", calc.add(5, 3))


# =========================================
# KEY CONCEPTS OF OOP
# =========================================

# - Class        → Blueprint for creating objects
# - Object       → Instance of a class
# - Encapsulation→ Wrapping data + methods together
# - Inheritance  → One class can use features of another
# - Polymorphism → Same method behaves differently
# - Abstraction  → Hiding unnecessary details


# =========================================
# CLASSES IN PYTHON
# =========================================

# A class acts like a template.
# You can create multiple objects using the same class.

class Dog:
    # Class attribute (shared by all objects)
    species = "Canis lupus"

    # Method (function inside a class)
    def bark(self):
        print("Woof!")

# Creating an object (instance of class)
my_dog = Dog()

# Accessing attribute
print("Species:", my_dog.species)

# Calling method
my_dog.bark()


# =========================================
# EXTRA: USING __init__ (Constructor)
# =========================================

# __init__ is a special method that runs automatically
# when an object is created.

class Student:
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object with values
s1 = Student("Akarsh", 20)
s1.display()


# =========================================
# SUMMARY
# =========================================

# OOP helps in writing clean, modular, and scalable code.
# It is widely used in real-world applications and large projects.

