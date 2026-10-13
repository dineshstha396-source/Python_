
# Day one of learning Python 

# Python Output

from cmath import pi


print("Hello World")

print("This is a python programming language")

print("I am learning python language")

print('Hello World')

print("Hello World")

print("This is the string")

print(3)

print(23)

print(True)

print(32.32)

print('Hello',1,2,False,21,21.2)

print("hello",1,2,21,sep="        ",end="\n\n\n\n\n\n")

print(1,2,2,3,"helor",end="n",sep=",,,,,,,,,,,,")


# Data Types

#integer
print(12)

#float
print(222222222.2333333333333333333)

#string
print('Hello World')
print("Hello World")
print("'Hello World'")
print('''Hello World''')
print('21')
print("212")

# Boolean 
print(False)

# Complex
print(4+5j)


# List 
print([1,2,3,"hello world"])


# Dictionary 
print({'name':"Dinesh", "roll":19})

# sets 
print({1,2,33,4})

# Tuple 
print((1,2,3,4,5))

# to know type : type()

print(type({12,2,12,21}))
print(type([1,2,3]))


# Variable 

name="Dinesh Shrestha"
print(name)

print("\n")

z=3223
print(z)

# Dynamics typing : way of variable declaration without giving its data type like in python 
# Static Typing : C, Java 

# Dynamic Binding  : meaning the data type of variable is changeble or dynamics 

a=2
print(a)
print(type(a))

a='the'
print(a)
print(type(a))

# comments : a line of sentence or text the wont be executed 

a=2 # inline comment
#single-line comment
print(a)

# there is not official multi line comment

# static binding : C, java 


a=12
b=32
c=32
print(a,b,c)

a,b,c=12,32,32
print(a,b,c)

a=b=c=3
print(a,b,c)

# Keywords and identifiers 

# Keywords : sets of words that are reserved for a specific purpose
# There are 32 keywords in python

# Identifiers : names given to entities like variable, function, class, module, etc.

# Rules 
# 1. Identifiers can contain letters, digits, and underscores
# 2. Identifiers cannot start with a digit
# 3. Identifiers cannot be a keyword
# 4. Identifiers are case sensitive
#5. Identifiers can be of any length
#6. Identifiers cannot contain special characters like @, $, %, etc.
#7. Identifiers cannot contain spaces


# User input : input() function is used to take input from the user

name=input("Enter your name: ")
print("Hello",name)

age=input("Enter your age: ")
print("You are ",name,"and age is ",age)

email=input("Enter your email: ")
print("Your email is ",email)

# WAP to take two numbers from the user and print their sum , difference, product .

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

sum=num1 + num2
diff=num1-num2
product=num1 * num2

print(f"The sum,difference,product of {num1} and {num2} is {sum},{diff},{product} respectively.")


#Type Conversion : Implicit vs Explicit 

#implicit type conversion : done by python automatically
#explicit type conversion : done by user using built-in functions like int(), float(), str(), etc.


# str -> int

a="12"
print(type(a))
print(type(int(a)))

# int to str 


a=12
print(type(a))
print(type(str(a)))

intege=int("12")
print(intege)

# Literals : the values stored in the variable 4

a=0b101001 # Binary Lieral
b=100 # Decimals 
c=0o310 # Octal Literal
d=0x12d # Hexadecimal Literal 

# String 

string='This is string'
strings="This is python"
char="C"
multiline_str="""This is multiline"""
# There are unicode and raw_str too

a=None
print(a)

# None can be used to preserve the variable name or for varialbe declaration for future use 
