# Python Tuple Practice

# Create an empty tuple, a one-element tuple and a tuple containing five mixed data types. Print their types.

empty=()
print(empty)
print(type(empty))

one=(1,)
print(one)
print(type(one))

mixed=(1,1.1,"1",True,(1,))
print(mixed)
print(type(mixed))

# Conver a string into a tuple of characters and a list of characters.

string='Apple'
tup=tuple(string)
li=list(string)

print(tup)
print(li)

# Given a tuple of 10 numbers, extract the first three, last three and every second element. 

tuple=(1,2,3,4,5,6,7,8,9,10)

print(f"Tuple : {tuple} \nThe first three : {tuple[:3]} \nLast three : {tuple[-3:]} \nEvery second : {tuple[1::2]}")

# Count the occurance of a specified values in a tuple and find its first index

tup=(1,2,3,4,5,5,3,4,2,3,5)
val=5

c_5=0
index=0

for i in tup:
    if val==i:
        c_5+=1
        if c_5==1:
            req=index
    index+=1

print(f"The occurance of {val} in '{tuple}' is {c_5} and first_index is {req}")

# Create a new tuple by replacing the second element of an existing tuple without modifying the original tuple 

t=(1,2,32,32,323,23,2)

new=t[:1]+(1212222222222,)+t[2:]

print(f"Original : {t} \nNew : {new}")