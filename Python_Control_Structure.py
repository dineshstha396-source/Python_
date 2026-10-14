# Day 2 of learning Python : Python Control structure/Statement 

# Operators 
"""
Arithmetic 
Relational 
Logical 
Bitwise 
Assignment 
Membership
"""

# 1. Arithmetic Operator
print(12+21)
print(12-12)
print(12/12)
print(12//12) # integer division
print(12*12)
print(12**12) # Power of 
print(12%12) # Modulus

# 2. Relational Operator 
print(12>12)
print(12>=12)
print(12<12)
print(12<=12)
print(12==12)
print(12!=12)

# 3. Logical operator 

print(1 and 0)

print(1 or 0)

print(not 2)

# 4. Bitwise Operators 

print(2 & 3) # bitwise and 
print(2 | 3) # bitwise or 
print(2 ^ 3) # bitwise xor
print(~ 3) #bitwise not 
print(4>>2) # bitwise left operator
print(4<<2) # bitwise right operator

# These are converted into binary code and respective calculation is done 

#5. Assignment Operators (=)

a=32
a+=2
print(a)
a-=3
print(a)

# Note a++ is not allowed

#6. Membership Operators (in/not in)

print("d" in "delhi")
print("d" not in "delhi")

print(2 in [21.21,21,21,4,2,2,9])



# Program : Find the sum of a 3 digit number entered by the user without loop

num=int(input("Enter a 3 digit number: "))
print(num)

sum=0 
rem=num%10
sum+=rem
num//=10
rem=num%10
sum+=rem
num//=10
rem=num%10
sum+=rem

print(sum)


# If-else in Python 

# simple Project 

"""
Login program and indentation project

Asumption
email: dstha3@gmail.com
password: 123
"""

email=input("Enter your email: ")
if email=="dstha3@gmail.com" :
    password=input("Enter your password: ")
    if password==123:
        print("Welcome")
    else:
        print("Enter the password correctly.")
else: 
    print("Not correct, please the correct email")


# Modulus 
# Similar kind of libraray or header file in C -> Modulus

import math 

print(math.sqrt(4))

import keyword

print(keyword.kwlist)

import random

print(random.randint(1,222222))

import datetime
print(datetime.datetime.now())

# List of modules in python

help("modules")

# Loops 

"""
While and for loop 
"""

# Table of n  using while loop 

n=int(input("Enter a number: "))
i=1
while i<11: 
    print(f"{n} * {i} = {n*i}")
    i+=1

# While loop with else 

x=12
while x< 322:
    print(x)
    x+=3
else:
    print("x is more than 322")


# Number Guessing Game 

# Generate a random integer between 1 to 100 
import random 
jackpot= random.randint(1,100)


flag=True
while flag:
    guess=int(input("guess the number: "))
    if guess > jackpot:
        print("The guess number is high")
    elif guess < jackpot:
        print("The guess number is low")
    else:
        print("You guess is correct. Congratulation.")
        flag=False

# Table of 3 using for loop 
for i in range(1,11):
    print(f"3 * {i} = {3*i}")

for i in {1,2,34,4,4}:
    print(i)

for i in [1,2,34,4,4]:
    print(i)

for i in (1,2,34,4,4):
    print(i)

for i in "kathmandu":
    print(i)


# Program : The current population of a town is 100000. The Population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the after 10 years. 

current=100000.00
print(f"The current population is {current}.")
grt_population=current
for i in range(1,11):
    grt_population=grt_population + grt_population*0.1
    print(f"The Population after {i} will be {grt_population:.2f}")


