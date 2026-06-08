'''
there are six main types of data types :
    1---> int ,eg:1,2,3,4,5,6,etc
    2---> str , eg:"a","b","shreyash",etc
    3---> float, eg:1.0,2.0,3.0,4.0,etc
    4---> bool, eg:True or False
    5--->NoneType, Represent Nothing
    6--->complex, eg: 1+2j,2+4j,etc
'''
print(type(26)) #int
print(type(26.0)) #float
print(type("twentysix")) #str
print(type(True)) #bool
print(type(None)) #NoneType
print(type(1+2j)) #complex

#------------------------------STRING & TYPE CONVERSION ------------------------------------------
"""
There is a unique code for every letter,special character,number 
this unique codes are known as unicode number or ascii
"""
#to find unicode of any character we just need to write ord(anything)
a=ord("A") #---->65
b=chr(65) #---->A
print(a)
print(b)

#--------------------------------STRING INDEXING --------------------------------------------------
name="shreyash"
 
#INDEXING
                      #  H   E   L   L   O 
                      #  0   1   2   3   4     -----> positive indexing


                      #  H   E   L   L   O 
                      # -5  -4  -3  -2  -1     -----> negative indexing

#  String Slicing

print(name[0:8])
print(name[0:6])
print(name[ : :-1])   # --------->  [start: stop : step]
print(name[0:8:2])
print(name[0:8:1])

#----------------------------------Type Converion ---------------------------------------
'''
there are two types of type conversion :
1)Implicit(automatic by python)----> (int/int)---float always
2)Explicit(manually done by the user)
'''
a=67
a=str(a)
print(type(a),a) #example of manual or Explicit type conversion
b=67/67
print(type(b),b) #example of automatic or Implicit type conversion
  
#Everything converts to true in bool except the following seven values 
"""
    1)0
    2)0.0
    3)False
    4)""
    5)[]
    6){}
    7)()
"""
a=0
a=bool(a)
print(a)
a=1
a=bool(a)    #bool conversion is always True except the seven values above 
print(a)
a=" "
a=bool(a)
print(a)