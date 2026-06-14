"""
Part 02 - Lecture 02
Topic: Strings & Conditional Statements
"""

# ======================================================
# 1. STRINGS
# ======================================================
# A string is a data type that stores a sequence of characters.

# ---------- Basic Operations ----------

# Concatenation
a = "hello"
b = "world"
print(a + b)
print(a + " " + b)

# Length of a string
a = "hello"
print(len(a))

b = "shreyash"
print(len(b))

# Example: find the length of the name entered by the user
name = input("Enter your name: ")
print(len(name))

# Use \n to start a new line inside a string
str1 = "This is a string.\nWe are creating it in Python."
print(str1)


# ---------- String Indexing ----------
#        H   E   L   L   O
#        0   1   2   3   4    --> positive indexing
#
#        H   E   L   L   O
#       -5  -4  -3  -2  -1    --> negative indexing

name = "shreyash"

# ---------- String Slicing : [start : stop : step] ----------
print(name[0:8])     # whole string
print(name[0:6])     # first 6 characters
print(name[::-1])    # reversed string
print(name[0:8:2])   # every 2nd character
print(name[0:8:1])   # same as name[0:8]


# ---------- Common String Functions ----------
text = "i am a coder."
print(text.endswith("er."))             # True  -> ends with "er."
print(text.capitalize())                # "I am a coder."
print(text.replace("coder", "singer"))  # replaces all occurrences
print(text.find("coder"))               # index of the first occurrence
print(text.count("am"))                 # how many times "am" appears


# ======================================================
# String Practice Questions
# ======================================================

# Q1: Input the user's name and print the length of the name
name = input("Enter your name: ")
print(f"The length of your name is {len(name)}.\nTHANK YOU")

# Q2: Count how many times "s" appears in a string (case-insensitive)
poem = ("Twinkle, twinkle, little star, How I wonder what you are! "
        "Up above the world so high, Like a diamond in the sky.")
print(poem.lower().count("s"))


# ======================================================
# 2. CONDITIONAL STATEMENTS
# ======================================================
# Statement       When to use it
# -------------   ---------------------------------------
# if              one condition to check
# if-else         two paths -> True or False
# if-elif-else    multiple conditions, checked one by one


# ======================================================
# Conditional Practice Questions
# ======================================================

# Q1: Accept two numbers and print the greater of the two
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

if a > b:
    print("a is greater than b")
elif b > a:
    print("b is greater than a")
else:
    print("a and b are equal")


# Q2: Accept gender from the user and print a greeting message
gender = input("Kindly enter your gender: ").strip().lower()

if gender == "male":
    print("Welcome, Sir")
elif gender == "female":
    print("Welcome, Ma'am")
else:
    print("Invalid input")


# Q3: Accept an integer and check whether it is even or odd
num = int(input("Enter any number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Q4: Accept age and check if the user is a valid voter (18+)
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Q5: Accept a year and check whether it is a leap year
year = int(input("Enter any year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The year {year} is a Leap Year")
else:
    print(f"The year {year} is not a Leap Year")


# Q6: Accept temperature in degrees Celsius and print a description
temp = int(input("Enter the current temperature: "))

if temp > 35:
    print("The temperature is extremely hot")
elif temp > 25:
    print("The temperature is slightly hot")
elif temp == 25:
    print("The temperature is pleasant")
elif temp >= 20:
    print("The temperature is slightly cold")
else:
    print("The temperature is very cold")

# Question 07
# Check whether the marks entered by the student are odd or even

marks = int(input("Enter the marks obtained by the student: "))

if marks % 2 == 0:
    print("The marks obtained by the student are even.")
else:
    print("The marks obtained by the student are odd.")


# Question 08
# Find the greatest of 3 numbers entered by the user

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if a >= b and a >= c:
    print("a is the greatest number")
elif b >= a and b >= c:
    print("b is the greatest number")
else:
    print("c is the greatest number")