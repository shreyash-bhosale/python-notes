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
a=456
digits=[]

digits.append(a%10)
a=a//10
digits.append(a%10)
a=a//10
digits.append(a%10)
a=a//10
for d in digits[::-1]:
    print(d)

a=int(input("enter the number:"))
digits=[]
while a>0:
    digits.append(a%10)
    a=a//10
for d in digits[::-1]:
    print(d)


