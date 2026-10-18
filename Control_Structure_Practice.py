# Practice Questions 


# Take two integers as input and print their sum, difference, product, quotient, floor division, remainder, and power.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

sum=num1+num2
diff=num1-num2
product=num1* num2
quotient=num1/ num2
floor_division=num1//num2
remainder=num1% num2
power =num1** num2

print(f"The sum, difference, product, quotient, floor division, remainder, and power of {num1} and {num2} are {sum}, {diff}, {product}, {quotient}, {floor_division}, {remainder} and {power} respectively.")

#Take an integer as input and check whether it is divisible by both 3 and 5 using logical operators.

integer=int(input("Enter a number: "))

if integer%3==0 and integer%5==0 : 
    print(f"{integer} is divisible by both 3 and 5.")
else:
    print("Not Divisible")


# 1. Take a number as input and use membership operators to check whether the digit "5" exists in its string representation. Also check whether "0" does not exist.

number=input("Enter a number: ")

if "5" in number: 
    print("5 exist")

if "0" not in number :
    print("0 doesnot exist.")


#Take an integer as input and determine whether it is positive, negative, or zero.

integer=int(input("Enter the number: "))

if integer>0:
    print(f"{integer} is positive.")
elif integer<0:
    print(f"{integer} is negative.")
else: 
    print(f"{integer} is zero.")


#Take three numbers as input and print the largest number using if-elif-else. Do not use max().

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

print(f"The entered three numbers are {num1}, {num2} and {num3}.")
if num1>=num3 and num1>=num2: 
    print(f"{num1} is the greatest.")
elif num2>=num1 and num2>=num3: 
    print(f"{num2} is the greatest.")
else: 
    print(f"{num3} is the greatest.")


# Write a login program that asks for an email and password. Display "Welcome" only when both are correct. Otherwise, print an appropriate error message.
# Assune : Email: stha3me@gmail.com and password =32 

email="stha3me@gmail.com"
password="32"

mail=input("Enter the email address: ")
pwd=input("Enter the password: ")

if mail==email and pwd==password: 
    print("Welcome")
else: 
    print("You got the wrong verification.")


"""
Take marks as input and assign grades using the following rules:
- 90–100: A
- 80–89: B
- 70–79: C
- 60–69: D
- Below 60: Fail
Reject marks below 0 or above 100
"""


marks=int(input("Enter the marks: "))

if marks>100 or marks <0:
    print("Marks entry invalid")
elif marks >=90: 
    print("You got A.")
elif marks>=80: 
    print("You got B.")
elif marks>=70: 
    print("You got C.")
elif marks>=60:
    print("You got D")
else: 
    print("You failed the exam.")



#Take an integer n as input and print its multiplication table from 1 to 10 using a while loop.

n=int(input("Enter a number for its multiplication: "))
flag=True
i=1
while flag: 
    print(f"{n} * {i} = {i*n} ")
    i+=1
    if i>10:
        flag=False

#Calculate the sum of all integers from 1 to \(n\) using a for loop.

n=int(input("Enter a number: "))

sum=0
for i in range(1,n+1):
    sum+=i

print(f"The sum of all integer from 1 to {n} is {sum}.")


# Take a positive integer as input and count its digits using a while loop. Do not convert the number to a string.

num=int(input("Enter the positive integer: "))

n=num
count=0
flag=True

while flag:
    if num==0:
        print(f"{n} contain {count} digits.")
        flag=False
    else: 
        num=num//10
        count+=1


# Print all even numbers between 1 and 100 using a for loop.

for i in range(1,101):
    if i%2==0:
        print(i)


#Take a number as input and calculate its factorial using a while loop.

num=int(input("Enter a number: "))

fact=1 

for i in range(1,num+1):
    fact*=i

print(f"The factorial of {num} is {fact}")


#Reverse an integer using a while loop. For example, 1234 becomes 4321.

num=int(input("Enter the integer: "))

n=num
flag=True
rev=0

while flag: 
    rem=num%10
    rev=10*rev+rem
    num=num//10
    if num==0:
        flag=False

print("The reverse of {n} is {rev}")