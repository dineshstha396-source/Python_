# Python Sets Practice 

# Create a empty set and an empty dictionary.

empty_s=set()
print(type(empty_s))
print(empty_s)

empty_d={}
print(type(empty_d))
print(empty_d)

# Convert a list with duplicate elements into a set. 

li=[1,1,2,3,3,4,5,5]

se=set(li)
print(li,se)

# Given two sets, calculate their union, intersection, difference and symmteric difference

set_1={1,2,3,4,5,6}
set_2={5,6,7,8,9,10}

print(f"The given sets are {set_1} and {set_2}")
print(f"Union : {set_1 | set_2} \nIntersection: {set_1 & set_2} \nDifference: {set_1 - set_2} \nSymmteric difference: {set_1^ set_2} ")

# Find the unique characters in a string using set.

string='tommorrow'

unique=set(string)

print(f"The unique character in '{string}' are:")
for i in unique:
    print(i)

# Count the number of distinct words in a sentence ignoring captilization.

sentence='Hello this is not a number hello this is a string'

distinct=set(sentence.lower().split(' '))

count=0
for i in distinct:
    count+=1

print(f"The number of distinct words are {count}")

# Given two lists of student IDs, find the IDs present in both lists.

li_1=[1,2,3,4,5]
li_2=[4,5,6,7,8]

print(f"The Students IDs that are present in both lists are: ")
for i in (set(li_1) & set(li_2)):
    print(i)

# Finds IDs that appears in the first list but not in the second


li_1=[1,2,3,4,5]
li_2=[4,5,6,7,8]

print(f"The Students IDs that are present in first lists but not in second are: ")
for i in (set(li_1) - set(li_2)):
    print(i)

# Find all IDs appearing in exactly one of two lists.


li_1=[1,2,3,4,5]
li_2=[4,5,6,7,8]

print(f"The Students IDs that are present in exactly one of two lists are: ")
for i in (set(li_1) ^ set(li_2)):
    print(i)

# Check whether two sets have no common elements using isdisjoint()

set_1={1,2,3,4,5,6}
set_2={5,6,7,8,9,10}

if set_1.isdisjoint(set_2):
    print("The set has no common elements.")

# Add several items to a set using update() and add()

set_1={1,2,3,4,5,6}
li=[]

for i in range(7,14):
    li.append(i)
    set_1.add(i)
print(set_1)

lis=[i**2 for i in li]

set_1.update(lis)
print(set_1)

# Given a list of email address , find duplicate address and return them as a set

li=['dstha3me@gmail.com','dstha3me@gmail.com','dstha2me@gmail.com']

se=set(li)

unique_li=list(se)
dup_li=[]

for i in unique_li:
    count=0
    for j in li:
        if j==i:
            count+=1
            if count>1:
                dup_li.append(i)
print(set(dup_li))
