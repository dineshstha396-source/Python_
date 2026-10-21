# Day 4 of Python Learning : Python List 

# Python List : It is a data type where you can store multiple items under 1 name.


#List vs Array 

"""
1. Array are fixed sized but list are not.
2. Array are homogenious meaning it can store only one type of data type iten but list are hetergenious.
3. Array are faster than Python List.
4. Array occupy less memory space than list.
"""
a=12
print(id(a))

# Characteristics of a List 
"""
1. Ordered 
2. Mutable
3. Hetergeneous
4. Can be nested 
5. Can have duplicate
6. can contain any kind of object in python 
7. Item can be accessed."""

li=[2,2,3]
lio=[2,2,3]

print(id(li))
print(id(lio))

# Creating a list 

#Empty 
print([])

# 1D
print([1,2,2])

# 2D
print([[1,2],[2,21]])

# 3D
print([[[1,2],[2,21]],[[212,21],[2,2]]]) # It is a homogeneous list

# Heterogeneous 
print([1,"hello",32,32.23,3+3j,True])

# Using Type Conversion
print(list(("hello",'WOrld','12')))


# Item accessing from the Python list

# Indexing

Li=[1,2,21,21]
print(Li[1])
print(Li[-1])
print(Li[0])

Li=[[21,2],[212,12]]
print(Li[0][1])
print(Li[1][-1])

# Slicing 
Li=[1,2,3,4,5,6,7,8,9,0]
print(Li[1:8])
print(Li[::2])


Li=[[21,2,32,3232,2,4,5,232,2],[21,32,2,3,5,342,3,43,42,2,12]]

print(Li[1])
print(Li[1][:4])
print(Li[:][:])


# Adding item to a list 

li=[2,21,21]

#Append
li.append(1)
print(li)

#extend
li.extend([1,"q"])
li.extend("fd")
print(li)

#Insert
li.insert(0,"helllo")
print(li)

# Editing items

Li=[1,2,3,24,54,54,34]
Li[0]=0
Li[-1]="f"
Li[1:3]="Hello"
Li[-2]="Oye"
print(Li)

# Deleting items 

# Using del : by index position

Li=[12,21,34,5,434,434,434,35,3430]

"""del Li
print(Li) : gives NameError: name 'Li' is not defined. Did you mean: 'li'?"""

del Li[0]
print(Li)

del Li[1:3]
print(Li)

# Remove 

Li.remove(434)

# pop

List=[212,21,4343,43,43,43,43,3,5,6,7]

List.pop(0)
List.pop() # delete the last as default is -1

print(List)

# Clear 

List.clear()
print(List)

# Operation in list

li1=[1,2,3]
li2=[4,5,6]

print(li1+li2)
print(li1*3)

print(1 in li1)

for i in li2:
    print(i)

# List function

li=[1,23,3,"t",[1,21],"t",True,0,32]
print(len(li))
print(li.count(1))
print(li.index("t")) # 1st occurance 

li=[212,221,21]
print(min(li)) # for homogenous data only
print(max(li))
print(sorted(li,reverse=True))
li.sort() # permanently
print(li)
li.reverse() # permanet
print(li)

L=li
print(id(L))
print(id(li))
print(L)

L=li.copy()
print(id(L))
print(id(li))
print(L)

# List comprehension

li=[x for x in range(1,11) ]
print(li)

li=[1,2,3]
s=3
li=[x*3 for x in li]
print(li)

li1=[x**2 for x in li]
print(li1)


li=[x for x in range(1,51) if x%5==0 ]
print(li)


langauge=['python','php','java','c','javascript']

langauge_p=[x for x in langauge if x.startswith("p")]
print(langauge_p)

# Traverse a list 

# itemwise
langauge=['python','php','java','c','javascript']
for i in langauge:
    print(i)

# Indexwise

for i in range(0,len(langauge)):
    print(langauge[i])


# Zip Function 

# write a program to add item of 2 list indexwise

li1=[12,2,2,1]
li2=[-12,-2,-2,-22]

print([x+y for x,y in zip(li1,li2)])

