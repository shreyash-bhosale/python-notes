'''
# Types at a Glance
        Statement	                                When to use it
            if	                            You have one condition to check
            if-else	                        Two paths — True or False
            if-elif-else	                Multiple conditions checked one by one
'''

#practise question:01
#Accept two numbers and print the greatest between them.
#---------------------------------code---------------------------------
a=int(input("enter the first number(a):"))
b=int(input("enter the second number(b):"))

if  a>b:
    print("a is greater than b")
else :
    print("b is greater than a")

#practise question:02
#Accept gender from user and print a greeting message.
#--------------------------------code--------------------------------------
a=input("Kindly Enter Your Gender:")
if a == "MALE":
    print("welcome sir")
elif a == "FEMALE":
    print("welcome mam")
elif a == "male":
    print("welcome sir")
elif a == "female":
    print("welcome mam")
else:
    print("invalid input")

#practise question:03
#Accept an integer and check if it is even or odd.
#-------------------------------code----------------------------------------------
a=int(input("enter any number:"))
if a%2==0:
    print("the number is even")
else:
    print("the number is odd")

#practise question:04
#Accept name and age — check if the user is a valid voter (18+).
#-----------------------------code------------------------------------------
a=int(input("enter your age:"))
if a>+18 :
    print("you are eligible to vote")
else:
    print("you are uneligible to vote")

#practise question:05
# Accept a year and check if it is a leap year.
#----------------------------code----------------------------------------
a=int(input("enter any year:"))
if a%4==0:
    print(f"the year {a} is a Leap Year ")
else:
    print(f"the year {a} is not a Leap Year")   

#practise question:06
# #Accept temperature in °C and print a description.
#-----------------------------code---------------------------------
a=int(input("enter the current temperature:"))
if a==25:
    print("the temperature is pleasant")
elif 35>a>25:
    print("the temperature is slightly hot") 
elif a>35:
    print("the temperature is extremely hot")
elif 20<a<25:
    print("the temperature is slightly cold")
elif   a<20:
    print("the temperature is very cold")


