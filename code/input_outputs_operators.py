#--------------------------------------OUTPUT---------------------------------------------------------
name="shreyash"
age=18

print("Hello World!")
print(f"my name is {name}") #----> Here the 'f' is used to tell the interpreter that the str can also include variables also
print(f"my age is {age}")
print("Name:",name , "Age:",age) #----> Multiple Value

#--------------------------------------INPUT--------------------------------------------------------
'''input() always return string to get int or float value we have to manually convert the text'''

name=input("Enter Your Name Here:")
age=int(input("Enter Your Age Here:"))

print("your name is ",name)
print("your age is ",age)
print(f"Hello {name},You are {age} years old.")

#-----------------------------------ARITHMETIC OPERATOR----------------------------------------------------
'''
    operator        name        example         result
        +       Addition         10+3             13
        -       subtraction      10-3              7
        *       multiplication   10*3             30
        /       division         10/3              3.333
        **      exponent         10**3          1000
        //      floor division   10//3             3
        %     modulus(remainder) 10%3              1
BODMAS
()-bracket
** - exponent
* / // % - multiplication, division , floor division, modulus
+ - - addition, subtraction

'''
#------------------------------------COMPARISION OPERATOR--------------------------------------------------
'''
Always return True or False.

        Operator    	Meaning     	Example     	Result
        ==	        Equal to	        5 == 5	        True
        !=	        Not equal to	    5 != 3	        True
        >	        Greater than	    5 > 3	        True
        <	        Less than	        5 < 3	        False
        >=	        Greater or equal	5 >= 5	        True
        <=	        Less or equal	    3 <= 5	        True
'''
#------------------------------------LOGICAL OPERATOR-------------------------------------------------
'''
        Operator	    Returns True when…	                        Example
        and	            Both conditions are True	            age > 18 and has_id == True
        or	            At least one condition is True	        is_admin or is_staff
        not	            Reverses the boolean	                 not is_banned
'''
#--------------------------------Assignment Operators-------------------------------------------
'''
        Operator	            Meaning          	Equivalent to
        +=	                Add and assign          	x = x + n
        -=	                Subtract and assign	        x = x - n
        *=	                Multiply and assign	        x = x * n
        /=	                Divide and assign	        x = x / n
        //=	                Floor divide and assign	    x = x // n
        %=	                Modulus and assign	        x = x % n
        **=         	    Power and assign        	x = x ** n
'''
