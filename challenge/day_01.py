# 🚀 CHALLENGE DAY 01 - Learning Python From Scratch

# VARIABLES & DATA TYPES

name = "Shreyash"   # storing a string (text) value in variable name
age = 18            # storing an integer (whole number)
marks = 95.5        # storing a float (decimal number)
is_student = True   # storing a boolean value (True/False)

print(name, age, marks, is_student)  # prints all variables together


# TYPE CHECKING

print(type(name))   # shows the data type of name (str)
print(type(age))    # shows the data type of age (int)
print(type(marks))  # shows the data type of marks (float)
print(type(is_student))  # shows the data type of is_student (bool)


# OPERATORS

# Arithmetic Operators
a = 10   # assigning value 10 to a
b = 3    # assigning value 3 to b

print(a + b)   # adds a and b → output 13
print(a - b)   # subtracts b from a → output 7
print(a * b)   # multiplies a and b → output 30
print(a / b)   # divides a by b → output 3.33...
print(a % b)   # gives remainder → output 1
print(a ** b)  # power → 10^3 = 1000

# Relational / Comparison Operators
print(a == b)  # checks if a is equal to b → False
print(a != b)  # checks if a is not equal to b → True
print(a > b)   # checks if a is greater than b → True
print(a < b)   # checks if a is less than b → False
print(a >= b)  # checks if a is greater or equal → True
print(a <= b)  # checks if a is less or equal → False

# Assignment Operators
a = 5       # assign value 5 to a
a += 2      # adds 2 to a → now a = 7
a -= 2      # subtracts 2 → now a = 5
a *= 2      # multiplies by 2 → now a = 10
a /= 2      # divides by 2 → now a = 5.0
a %= 2      # remainder when divided by 2 → now a = 1.0
a **= 2     # square of a → now a = 1.0

# Logical Operators
print(not False)        # reverses False → True
print(True and False)   # both must be True → False
print(True or False)    # one True is enough → True


# TYPE CONVERSION (AUTOMATIC)

a, b = 1, 2.0   # a is int, b is float
sum = a + b     # Python converts int to float automatically
print(sum)      # prints result (3.0)


# TYPE CASTING (MANUAL)

a, b = 1, "2"   # b is string
c = int(b)      # converting string "2" into integer 2
sum = a + c     # adding both integers
print(sum)      # prints result (3)


# INPUT IN PYTHON

name = input("Enter your name: ")   # takes input from user as string
print(name)   # prints the entered name

age = int(input("Enter age: "))   # takes input and converts to integer
print(age)   # prints the age

marks = float(input("Enter marks: "))  # takes input and converts to float
print(marks)   # prints the marks


# PRACTICE QUESTIONS

# 1. Input 2 numbers & print their sum
a = int(input("Enter first number: "))   # taking first number
b = int(input("Enter second number: "))  # taking second number
print("Sum =", a + b)   # printing sum of both numbers


# 2. Input side of a square & print area
side = float(input("Enter side: "))   # taking side length
print("Area =", side * side)   # area = side × side


# 3. Input 2 floating numbers & print average
a = float(input("Enter first number: "))   # first number
b = float(input("Enter second number: "))  # second number
print("Average =", (a + b) / 2)   # average formula


# 4. Input 2 integers & check a >= b
a = int(input("Enter a: "))   # input first number
b = int(input("Enter b: "))   # input second number
print(a >= b)   # prints True if a >= b, otherwise False