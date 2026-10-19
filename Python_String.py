# Day 3 of Learning Python : Python String 

# Creating String 

print('String')
print("String's")
print('''this
is a string and long''')

# Access substring from string 
# Index

s='This is the best thing i know'
print(s[12])
print(s[-9])

#Slicing
print(s[0:10])
print(s[::-1])

#Editing and Deleting the string 

#Python string are immutable
# del for deleting


"""print(s)
del s
print(s) : Name Error"""


# Operation in Strings 
a="str"+"ing"
print(a)

a="*" *50
print(a)

print("str">"str")
print("str"<"str")
print("str"=="str")
# small alphabet > capital alphabet


# "" : Empty string is false
# "Not Empty" is True

print(not "")
print(not " ")

print("D" in "Dinesh")

for i in "Dinesh":
    print(i)

# Functions of Pytho Strings 

# Common
print(len("Dinesh Shrestha")) # Including Space
print(max("Dinesh Shrestha"))
print(min("Dinesh_Shrestha"))
print(sorted("Dinesh Shrestha"))# assending by default with list as output


s="DInesh ShrestHa"
print(s.title())
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())


f="Hari Shrestha"
print(f.count("H"))
print(f.find("H")) 
print(f.index("H"))  # index give error when we try to find the value not in the string 


g="Aakriti Thapaliya"
print(g.endswith("liya"))
print(g.startswith("A"))

first_name="Jayana"
last_name="Pradhan"

print("One of my classmate is {} {}".format(first_name,last_name))


a="Apple123"
print(a.isalnum())
print(a.isnumeric())
print(a.isdigit())
print(a.isidentifier())


a="This is the best part"
print(a.split("t")) # Its split the words based on delimeter with space as default and list as output format

li=['This is ', 'he bes', ' par', '']
print("t".join(li))


print(first_name.replace(first_name[2],"OYE"))

o="      this is the           best thing       "
print(o.strip())
print(o.rstrip())
print(o.lstrip())