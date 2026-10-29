# Day 8 of Python : Python function 

# Function 

def is_even(num):
    """This function return the given number is odd or even.
    input : any integer 
    output: odd/even
    created on : 10/22/2026"""
    if num%2==0: 
        return 'even'
    else :
        return 'odd'

for i in range(1,11):
    x=is_even(i)
    print(f"{i} : {x}")

# access docstring 

print(is_even.__doc__)

print(print.__doc__)

# Type of argument 

# default 

def power(a=1,b=1):
    return a**b

print(power())

# positional 

print(power(2,3))

# Keyword 

print(power(b=3,a=2))


"""
*args and **kwargs 
= These are special python keywords that are used to pass the variable length of arguements to a function

*args allows us to pass a variable number of non-keyword arguments to a function. : tuple 

**kwargs allows us to pas any number of keyword arguments.  : dictionary

Keyword arguements mean that they contain a key-value pari, like a python dictionary.

Note : 

i. order of the arguments matter (normal -> args -> **kwargs)
ii. The words 'args' and "kwargs" are only a convention, you can use any name of your choice
"""
#args
def mulitply(*args):
    product=1
    for i in args:
        product*=i
    return product

print(mulitply(1.2,2,2,4,232,32,2))


# kwargs 

def display(**kwargs): 
    print(kwargs)
    for i,y in kwargs.items():
        print(f"{i} : {y}")

display(nepal='best',inida='12')

# None is the default return value if not given in the function block 

def s(sd):
    print("f")
print(s(3))

# Nested Function 

def f():
    def g():
        print("Hello bro")
    print("yes")
    g()

f()

# Function in python are first class citizen

# type and id

def cube(num):
    return num**3
print(type(cube))
print(id(cube))

# reassign 

x=cube 
print(x)
print(type(x))
print(x(2))

# deleting a function 

def s(sd):
    print("f")
print(s(3))

"""del s

print(s(3)): NameError: name 's' is not defined"""

# Storing 

L=[1,2,21,cube]

print(L)

# Returning a function

def f():
    def x(a,b):
        return a+b
    return x

val=f()(3,4)
print(val)

# function as argument 

def func_a():
    print("Inside func_a")

def func_b(z):
    print("Inside func_c")
    return z()

print(func_b(func_a))

# Lambda function 

""" A Lambda function is a small anonymous function.
It can take any number of arguments, but can only have one expression."""

# for square 

a=lambda x : x** 2 

print(a(2))

# for sum

x=lambda a,b: a+b

print(x(2,2))

print(x(3,32))

"""
Difference between normal and lambda 

- no name 
- lambda has no return value but returns a function 
- it is written in 1 line 
- no reusable 

they are used with Higher order functions 

"""

# Check if a string has "a"

a= lambda s : "a" in s
print(a("Hds"))

# odd or even 
a= lambda a :  'even'  if a%2==0  else "odd"
print(a(32))

