# 50 Practice Questions on the topics i studied yesterday on Python Fundamental

#1. Print Hello, Python! on the screen.

print("Hello, Python!")

#2.Print your name, age, and country on three separate lines.

print("Name: Dinesh Shrestha \nAge:19 \nCountry: Nepal")

#3.Print the numbers 10, 20, and 30 using one print() statement.

print(10,20,30)

#4. Print Python, SQL, and Statistics separated by |. 

print("Python","SQL","Statisitcs",sep="|")

#5. Print Hello without moving to the next line, then print World.

print("Hello",end=" ")
print("World")


#6. Use sep to display 1-2-3-4-5.

print(1,2,3,4,5,sep="-")

#7. Use end to print Learning and Python on the same line using two separate statements.

print("Learning",end=" ")
print("python")

#8
"""Predict the output:

print("A", "B", "C", sep="---", end="!")
print("D")

Answer : A---B---C!D


"""

#9

""" Predict the output:
print(10, True, "20", 3.5, sep=" | ")
Answer: 10 | True | 20 | 3.5
"""

#10

"""Write a program that prints the following exactly:
===== REPORT =====
Name: Dinesh
Subject: Python
==================

"""

print("===== REPORT =====","Name: Dinesh","Subject: Python","====================",sep="\n")

#11. Print one example of each of these: integer, float, string, Boolean, and complex number.

print(12) # int
print(2.2) # float
print("2f") # string
print(True) # Boolean 
print(2+3j) # complex


# 12. Display the type of 25.

print(type(25))

#13. Display the type of 25.0. Explain how it differs from Question 12.

print(type(25.0))

"""12 number is integer and 13 number is float as it has decimal point which make it differ"""

#14. What is the type of "25"?

# Answer : str

#15. What is the type of False?

# Answer : bool 

# 16. Find the type of 3 + 4j.

print(type(3+4j))

#17. Find the type of [1, 2, 3].

print(type([1,2,3]))

#18. Find the type of (1, 2, 3).

print(type((1,2,3)))

#19. Find the type of {"name": "Ram", "age": 20}.

print(type({"name": "Ram", "age": 20}))

# 20

"""Predict the types and outputs:
print(type({1, 2, 3}))
print(type({}))
print(type(()))
print(type(None))

Answer : set, dict, tuple, None
"""

print(type({1, 2, 3}))
print(type({}))
print(type(()))
print(type(None))

# 21. Create variables for your name, age, GPA, and whether you are a student. Print all four.

name="Dinesh Shrestha"
age=19
GPA=3.64
isStudent="I am a student"

print(f"Hi, My name is {name} and i am {age} years old.{isStudent} with GPA: {GPA}")

#22. Assign 100 to a variable named score and print it.

score=100
print(score)

#23. Assign a value to x, then change it to a different value. Print both values by using a print statement after each assignment.

x=12
print(x)

x=122
print(x)

#24
"""Predict the output:
a = 10
a = 20
print(a)

Answer =20
"""

# 25. Assign 5, 10, and 15 to a, b, and c in a single statement.

a,b,c=5,10,15

# 26. Assign the value 100 to three variables in one statement.

x=y=z=100

#27 
"""Predict the output:
x = 5
y = x
x = 10
print(x, y)

Answer : 10,5
"""

#28. Create a variable called data, first store an integer, and then store a string. Print its type after each assignment.

data=12
print(data)
print(type(data))

data="Hello"
print(data)
print(type(data))

#29. Swap the values of a = 10 and b = 20 using Python assignment syntax, without creating a temporary variable.

a=10
b=20

b,a=a,b
print(a)
print(b)

#30. Explain the difference between dynamic typing and dynamic binding in your own words. Research or test any part you're unsure about.

"""Dynamic typing mean declaration or use of variable without assigning its data type which is done by the python itself internally
While dynamic binding mean the data type of the variable is not rigid and may changes in the code as per the value assign to the variable."""

"""Is student_name a valid identifier?
Yes

Is student2 valid?
Yes


Is 2student valid? Why?
No, as it is starting with number

Is first name valid?
No

Is total_marks valid?
Yes

Is class valid as a variable name?
NO

Are age and Age the same identifier?
No

Is total$amount valid?
NO
"""

#39

"""Correct the invalid variable names:
1name = "Ram"
student name = "Hari"
class = 10

"""
name="Ram"
student_name="Hari"
grade=10

# 40 

"""Which of the following are valid Python identifiers? For each invalid one, explain why.
_name = 10 :Yes
2name = 20 : No, as it is starting from digits
first_name = 30:  Yes
first-name = 40 : No, as special characters are not allowed
class = 50 : No, as keywords can't be used 
Class = 60 : Yes
__value__ = 70 :Yes
total$ = 80: NO, as special character are not allowed 
name2 = 90 : Yes
True = 100: No, as True can't be used""" 


#  Q41. Ask for a student's name, age, and GPA. Convert age to int and GPA to float. Display a formatted report and the type of each converted value.

stu_name=input("Enter your name: ")
age=int(input("Enter your age: "))
GPA=float(input("Enter your GPA: "))

print(f"The name of the student is {stu_name} with age {age} and GPA {GPA}.")

print(type(stu_name))
print(type(age))
print(type(GPA))

# Q42. Write a calculator that accepts two integers and displays their sum, difference, product, quotient, floor division, and remainder. Format the output using f-strings.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

sum=num1+num2
difference=num1-num2
product=num1*num2
quotient=num1/num2
floor_division=num1//num2
remainder=num1%num2

print(f"The sum,difference,product, quotient, floor division and remainder are {sum}, {difference}, {product}, {quotient}, {floor_division} and {remainder} respectively. ")

# Q43. Ask for three subject marks and calculate the total and average. The marks must be entered by the user, not hardcoded.

sub1=int(input("Enter the first subject mark: "))
sub2=int(input("Enter the second subject mark: "))
sub3=int(input("Enter the third subject mark: "))

total=sub1+sub2+sub3
average=total/3

print(f"The total and average of {sub1}, {sub2}, {sub3} are {total} and {average} respectively. ")

# Q44. Ask for a product's price and quantity. Calculate the subtotal, a 13% tax, and the final bill. Accept the price as a decimal number.

product=input("Give me the name of the product: ")
price=float(input("Enter the price of the product: "))
quantity=int(input("Enter the quantity of product: "))

subtotal=price*quantity 
tax_amt=0.13*subtotal
fianl_total=subtotal+tax_amt

print(f"The total cost for {product} is {fianl_total}")

# 45

""" Predict the output and explain each conversion.
a = "12"
b = 3

print(a * b) # 121212
print(int(a) * b) # 36
print(float(a) + b) # 36.0
print(str(b) + a) # 312

"""

# Q46. Write a program that accepts a number as a string, converts it into an integer and a float, and displays each value with its data type. What happens if the input is "12.5" and you attempt int() directly?

num=input("Enter a number: ")
print(num)
print(type(num))

integer=int(num)
print(integer)
print(type(integer))

decimal=float(num)
print(decimal)
print(type(decimal))

# 47

"""Predict the output and explain implicit conversion.
a = 7
b = 2.5
c = a + b
d = int(c)

print(c, type(c)) : 9.5,float
print(d, type(d)) : 9,int 
print(str(c) + str(d)) : 9.59

Ezplaination: int (a) changed to float
"""


# 48 

"""Convert these binary, octal, and hexadecimal literals to decimal values. Write a program that prints all results.
a = 0b101101
b = 0o64
c = 0x3A
"""
a = 0b101101
b = 0o64
c = 0x3A
print(a,b,c)

# 49 

""" Identify which literals are invalid and explain why the code fails.
a = 0b10102 : 2 is invalid
b = 0o78 : 8 is invalid
c = 0x2F
d = 0b1111

print(a, b, c, d)
"""

# Q50. Create a variable result initialized to None. Later, assign it the sum of two user-entered numbers. Print the value and type before and after assignment. Explain why None differs from 0 and "None".

result=None
print(result)
print(type(result))

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

result=num1+num2
print(result)
print(type(result))

"""None mean nothing or similar to Null but 0 is an integer with type int and has meaning of zero and "None" mean string of value None"""