# Practice Question 

# Find the length of a given string without the len() function. 

s=input("Enter the string: ")

count=0 

for i in s:
    count+=1

print(f"The length of {s} is {count}.")

# Extract the username from the given email

s=input("Enter the email: ")

print(s.split("@")[0])

# or 

p=s.index("@")
print(s[0:p])

# Count the frequency of a particular character in a provided string. 

s=input("Enter the string: ")

term= input("What would you like to search for ? ")

count=0

for i in s:
    if i == term: 
        count+=1

print(f"The frequency of {term} is {count}")

# Write a program to remove a particular character in a given string

s=input("Enter the string: ")

term= input("What would you like to search for ? ")

result=""

for i in s: 
    if i!=term:
        result+=i
print(result)

# Write a program that can check whether a given string is palindrome or not. 

s=input("Enter the string: ")

flag=True
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        flag=False
        print("Not a palindrom")
        break
    if flag: 
        print("Palindrome")

