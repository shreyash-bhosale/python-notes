
'''
#palindrome check!
a=int(input("enter the number:"))
copy =a
rev=0
while a>0:
    digit=(a%10)  #last digit
    rev=(a*10)+digit
    a=a//10
if copy==rev:
    print("the number is a palindrome!")
else:
    print("the number is not a palindrome")

# now here is a thing to understand that this code check the  palindrome condition 
 only for the "a" if we want to check for any other numberwe have to write the code again 
 to solve this thing w have functions!

'''
"""
Functions in Python

What are Functions?
A function is a block of code designed to perform a specific task. Instead of repeating the same code again and again, you can define it once and reuse it whenever required.

def greet():
    print("Hello, welcome to Python!")

greet()   # function call
"""
#example no 01
def hello():
    print("hello world")
    print("welcome to mumbai ")
hello()    #-------> if we don't call hello() the code will no execute and we will not get any output and we can use this hello() to run  the code again and again
hello()    #------->runs second time
hello()    #------->runs third time

#make the palindrome checker into a user defined function:
def palindrome_check(a):
    copy=a
    rev=0

    while a>0:
        digit=(a%10)
        rev=(rev*10) + digit
        a=a//10
    if copy==rev:
        print("the number is a palindrome")
    else:
        print("the number is not a palindrome")
palindrome_check(int(input("enter the number for which you want to check the palindrome:")))

#parameter :The variable name in the function definition. Like a placeholder.
#argument:The actual value you pass when calling the function.

#types of argument:
# 1. Positional — order matters
def add(a, b):
    return a + b
add(5, 3)       # → 8

# 2. Default — works even without passing a value
def greet(name="Guest"):
    print(f"Hello {name}")
greet()            # Hello Guest
greet("Akarsh")  # Hello Akarsh

# 3. Keyword — pass in any order
def info(name, age):
    print(f"{name} is {age}")
info(age=25, name="Akarsh")  # order doesn't matter
