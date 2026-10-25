#  Python string practice questions 

# Create a string containing your full name and print it using single quotes, double quotes and triple quotes. 

my_name='Dinesh Shrestha'
print(my_name)

my_name="Dinesh Shrestha"
print(my_name)

my_name='''Dinesh Shrestha'''
print(my_name)


# Store the word 'Data Analytics ' and print it length, first character , last character and middle character. 

word='Data Analytics'

print(f"The length of {word} is {len(word)}.")

print(f"The first,middle and last character of {word} is {word[0]}, {word[len(word)//2]} and {word[-1]} respectively. ")

#Predict the output of s = "PYTHON"; print(s[1], s[-2], s[1:4], s[:3], s[3:])
#before running it.
"""
Output: 
Y
O
YTH
PYT
HON
"""

# Reverse a string using slicing and looping  .

# Slicing 

string="HEllo world"
print(string[::-1])

# Looping 
j=1
for i in string: 
    print(string[len(string)-j],end="",)
    j+=1


# Extract "Analytics" from "Data Analytics Foundation" using slicing only.

print("\n")
string="Data Analytics Foundation"


for i in range(0,len(string)):
    if string[i]=="A":
        for j in range(i,len(string)):
            print(string[j],end="")
            if string[j]=="s":
              break
       

# Print every second character of a string starting from index 0 . then print every second character starting from index 1. 

print('\n')
string=input("Enter a sentence: ")

# Starting from index 1

index=1
for i in string[1:]:
    if index%2==0:
        print(i,end='')
    index+=1
print('\n')

# Starting from index 0
index=0
for i in string[:]:
    if index%2!=0:
        print(i,end="")
    index+=1
print('\n')

# Check whether a given string is a palindrome , ignoring capitalization and surrounding spaces. 

string=input("Enter a word: ")

flag=False
for i in range(0,len(string)//2):
    if string[i]==string[len(string)-i-1]:
        continue
    else: 
        flag=True
if flag:
    print("It is not palindrome.")
else:
    print('It is palindrome.')

# Count the vowels, constants ,digits , spaces and special character in a string. 

sentence=input("Enter a sentence: ")

c_v=0
c_c=0
c_d=0
c_s=0
c_sc=0

for i in sentence: 
    if i.isalpha():
        if i in ["a",'e','i','o','u','A','E','I','O','U']:
            c_v+=1
        else:
            c_c+=1
    elif i.isdigit():
        c_d+=1
    elif i==" ":
        c_s+=1
    else:
        c_sc+=1

print(f"\n The count of vowels, constants ,digits , spaces and special character in a '{sentence}'is {c_v}, {c_c}, {c_d}, {c_s}, and {c_sc} respectively. ")


# Given a full name, count the number of words without counting extra spaces at the beginning or end.

name=input("\nWhat is your name?\n")

name=name.strip()

i=0
for j in name: 
    if j==" ":
        i+=1
    else:
        continue
print(f"\nIn {name}, There are {i+1} words")

# Convert "dATA sCIENCE" into lowercase, uppercase, title case, and sentence-style capitalization. Explain the difference between title() and capitalize().

original="dATA sCIENCE"

print(f"\n Original : {original} \n Lowercase : {original.lower()} \n Uppercase : {original.upper()} \n Titlecase : {original.title()} \n Captilize : {original.capitalize()}.")