#------------------------RANGE------------------------
'''
range(stop)             # from 0 upto stop-1
range(start,stop)       # start upto stop-1
range(start,stop,step)  # start,jumping by step
'''
list(range(5))      #[0, 1, 2, 3, 4]
list(range(1,6))    #[1, 2, 3, 4, 5]
list(range(0,10,2)) #[0, 2, 4, 6, 8]

'''for i in range(10,21,1): #--------------> print no from 10 to 20 
    print(i)

for i in range(1,101,1): #-----------------> print no from 1 to 100
    print(i)

for i in range(5,51,5): #------------------> print table of 5
    print(i)
'''
#---------------------------------LOOPS X VARIABLES---------------------------------------
#----------------------------FOR LOOPS-----------------------------------------------
# making a program to take a input from the user and print the table of the input number.
#--------------------------------------code-----------------------------------------------------------
'''
n=int(input("enter the number of which you want the table:"))

for i in range(n,(n*10)+1,n):
    print(i)
'''
#----------------------------------LOOPS X STRINGS --------------------------------------------------
'''
a="Shreyash"
for i in a:
    print(i)
'''
'''
a="Shreyash"
for i in range(0,len(a)-2,1):
    print(f"{i}:{a[i]}")
'''
#----------------------------BREAK ,CONTINUE AND ELSE --------------------------------------
#break completely stops the loop 
#continue skip the current itteration and starts the next one 
#
'''
for i in range(1,11):  #-------------> example of break 
    if i==4:
        break
    print(i)

for i in range(1,11): #----------> example of continue 
    if i==5:
        continue
    print(i)

#multiple uses
for i in range(1,21):  -------------> use of both break and continue together
    if i==5 or i==6 or i==7:
        continue
    elif i==10:
        break
    print(i)
'''
#use of else
''' 
for i in range(1,11):
    if i==12:
        break           #  ---->if the loop break then else will not run and if it doesn"t break than else condition will run
    elif i==1 or i==6 or i==7:
        continue
    print(i)
else:
    print("no break encountered!!")
'''
'''
#------------------------------------PRACTISE QUESTIONS-------------------------------------
# question no 01
#Print "Hello World" n times
 
#-------------------------------------CODE------------------------------------------
n=int(input("enter the number of times you want to print HELLO WORLD: "))
for i in range(n):
    print("HELLO WORLD")

#question no 02
#Print natural numbers from 1 to n.
#-------------------------------------CODE------------------------------------------
n=int(input("enter the number"))
for i in range(1,n+1,1):
    print(i)

#question no 03
#Reverse for loop — print n down to 1.
#-------------------------------------CODE------------------------------------------
n=int(input("enter the number:"))
for i in range(n,0,-1):
    print((i))

#question no 04
#Print the multiplication table of a number.
#-------------------------------------CODE------------------------------------------
n=int(input("enter the number"))
for i in range(n,(n*10)+1,n):
    print(i)

#question no 05
#Sum of first n natural numbers.
#-------------------------------------CODE------------------------------------------
n=int(input ("enter the number:"))
total=0
for i in range(1,n+1,1):
    total+=i

print("Sum = ",total)

#question no 06
#Factorial of a number.
#-------------------------------------CODE------------------------------------------
n=int(input ("enter the number:"))
factorial=1
for i in range(1,n+1,1):
    factorial*=i

print("factorial = ",factorial)

#question no 07
#Print sum of all even and odd numbers in a range separately.
#-------------------------------------CODE------------------------------------------
n=int(input ("enter the number:"))
odd=0
even=0
for i in range(1,n+1,1):
    if i % 2 !=0:
        odd+=i
    elif i % 2 ==0:
        even+=i
print("the sum of the even is :",even)
print("the sum of the odd is :",odd)

#question no 08
#Print all factors of a number.
#-------------------------------------CODE------------------------------------------
n=int(input("enter the number:"))
for i in range(1,n+1,1):
    if n % i == 0:
        print(i)

#question no 09
#Check if a number is perfect (sum of factors = the number itself).
#-------------------------------------CODE------------------------------------------
n=int(input ("enter the number:"))
j=0
for i in range(1,n):
    if n % i == 0:
        j += i

if j==n:
        print("the number is a perfect number")
else:
        print("the number is not a perfect number")

#question no 10
# Check if a number is prime.
#-------------------------------------CODE------------------------------------------
n=int(input ("enter the number:"))


if n <= 1:
        print("the number is not a prime number")
else:
    for i in range(2,n):    
        if n % i == 0 :
            print("the number is a not a prime number")
            break
    else:
        print("the number is a prime number")

#question no 11
# Reverse a string without using built-in functions.
#-------------------------------------CODE------------------------------------------
n=input ("enter the string:")
for i in range(len(n)-1,-1,-1):
    print(n[i], end="")

#question no 12
#Check if a string is a palindrome.
#-------------------------------------CODE------------------------------------------
n=input ("enter the string:")
if n ==n [::-1]:
    print("it is a palindrome ")
else:
    print("no palindrome")

#question no 13
#Count letters, digits, and special symbols in a string.
#-------------------------------------CODE------------------------------------------
n=input ("enter the string:")
alphabet=0
number=0
special=0

for ch in n:
    if ch.isalpha():
        alphabet+=1
    elif ch.isdigit():
        number+=1
    else:
        special+=1

print("letters=",alphabet)
print("number",number)
print("apecial characters",special)

#---------------------------EXTRA PROBLEMS-----------------------------
#question no 14:
#star pattern:Print a right-angled triangle of stars with n rows using nested for loops.
#----------------------------------CODE--------------------------------
n=int(input("enter the numbers of row :"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

#question no 15:
#Number Triangle Pattern
#------------------------------------CODE---------------------------------------
n=int(input("enter the numbers of rows:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#question no 16:
#Print the triangle upside down.
#------------------------------------CODE---------------------------------------
n=int(input("enter the number of rows :"))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print("*",end=" ")
    print()

# question number 17:
#Print the row number repeated on each row.
#------------------------------------CODE---------------------------------------
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range (1,i+1):
        print(i,end=" ")
    print()
'''



