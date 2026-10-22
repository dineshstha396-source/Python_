# Day 5 Of Python :Python tuple

# Tuple 

# Creating Tuple 

# Empty 
t1=()
print(t1)

# Single items
t1=(2)
print(type(t1))
print(t1)

t1=(2,)
print(type(t1))
print(t1)

# Homo 
t1=(21,21,3,3,3)
print(type(t1))
print(t1)

# Hetero
t1=(2,21,"e",True)
print(type(t1))
print(t1)

#tuple 

t1=(1,2,(2,21))
print(type(t1))
print(t1)

# Type conversion 

t1=tuple("Hello")
print(type(t1))
print(t1)

# Accessing items 

# similar to list 
t1=(21,21,21,1,1)
print(t1[1])

# Editing item 

# Note : Python tuple can't be changed .

# Adding item 

# Note : Python tuple is immutable 

# Deleting items 

t1=(21,21)
print(t1)
"""del t1
print(t1) : NameError: name 't1' is not defined """

# Operation and function on tuple 

# Similar to python 

"""
Difference Between Python list and tuple 

1. syntax: list [] and tuple()
2. Mutability : List is mutable
3. Speed : Tuple is faster 
4. Memory : Tuple occupy less memory space 
5. Built in function : Tuples has less than list 
6. Error prone : List is more
"""

# special syntax

# tuple unpacking
a,b,c=(1,2,3)
print(a)

"""
a,b,c=(1,3)
print(b) : ValueError: not enough values to unpack (expected 3, got 2)
"""
a,b,*others=(1,2,3,32,32,32)
print(a)
print(others) # Gives list 

d=1
s=2
print(d,s)

d,s=s,d
print(d,s)

# ziping tup;es 

a=(3,3,234,553)
b=(32,32321,3243,43)

print(tuple(zip(a,b)))