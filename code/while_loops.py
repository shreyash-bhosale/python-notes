'''
while True:           ------------>if true the condition will run infinitely!
    print("hello")
'''
'''
a=1
while True:          ---------------->here used for printing no from 1 to infinity
    print(a)
    a=a+1

#example:write a code to print no from 1 to 20
a=1
while a!=20:
    print(a)
    a=a+1
'''
#question no :01
#Separate each digit of a number and print on a new line
#------------------------------------CODE---------------------------------------
'''
a=int(input("enter the number:"))
digits=[]            ---------- ------------->manual way 

digits.append(a%10)
a=a//10
digits.append(a%10)
a=a//10
digits.append(a%10)
a=a//10
for d in digits[::-1]:
    print(d)

# ---------------by using while loop----------------
a=int(input("enter the number:"))
digits=[]
while a>0:
    digits.append(a%10)
    a=a//10
for d in digits[::-1]:
    print(d)
 #question no :02
 #Accept a number and print its reverse.
a=int(input("enter the number:"))
rev = 0
while a>0:
    digit= a % 10           #last digit-remainder
    rev = rev*10 + digit 
    a = a//10               #remove the last digit

#question no : 03
#Check if a number is palindromic (equal to its reverse).
n = int(input("Enter a number: "))
original = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if original == rev:
    print("Palindrome number")
else:
    print("Not a palindrome")

#question no :04
#Build a number guessing game — computer picks a random number, user keeps guessing until correct.
import random
secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f" Correct! You guessed it in {attempts} attempts.")
        break
'''


