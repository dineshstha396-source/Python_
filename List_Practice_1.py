# Python List Practice



# Create an empty list and add five integers using append().
empty=[]
print(empty)

#   Adding integer
for i in range(0,5):
    empty.append(i)

final=empty
print(final)

# Create a list containing integers, strings, floats, booleans, and another list. print its lengtha nd the type of every elements. 

mixed=[1,1.1,"1",True,[1]]

print(f"The length of the list is {len(mixed)} \nThe data type of each element is given below: ")

for i in mixed:
    print(f"{i} : {type(i)}")

# Given a list of 10 numbers, print the first three , last three and middle four and reversed list.

integer=[1,2,3,4,5,6,7,8,9,10]

print(f"The first three : {integer[:3]} \nTHe last three : {integer[-3:]} \nThe midde four : {integer[3:7]} \nReversed List : {integer[::-1]}")

# Given a list, repalce its second, fourth and last elements with new values. 

integer=[1,2,3,4,5,6,7,8,9,10]
print(f"Initial Values : {integer}")

integer[1]='12'
integer[3]=32
integer[-1]=323

print(f"Final Values : {integer}")
# Remove every occurence of a given value from a list without using remove()


li=[1,2,2,2,1,1,2,1,2,11,1,1]
remove=1
new_li=[]

for i in li:
    if i!=remove:
        new_li.append(i)

print(new_li)

# Find the largest and smallest values without using max() or min().

li=[12,2,21,21,3,2,43,5,44,45656,5555555]
large=li[0]
small=li[0]

for i in li:
    if i>large:
        large=i

print('largrst value: ',large)


for i in li:
    if i<small:
        small=i

print('Smallest value: ',small)


# Calculate the sum,average, count and range of a list of a number.

li=[1,2,3,4,5,6,7,8,9,10]

large=li[0]
small=li[0]

for i in li:
    if i>large:
        large=i

for i in li:
    if i<small:
        small=i

print(f"The given list : {li}  \nThe sum : {sum(li)} \nThe average: {sum(li)/len(li)} \nThe lenth : {len(li)} \nThe range : {large-small}")


# Count how many numbers are even, odd, positive, negative and zero.

li=[12,2,3,4,43,43,23,232,1]
c_odd=0
c_even=0
c_pos=0
c_neg=0
c_zer0=0

for i in  li:
    if i % 2==0:
        c_even+=1
    else:
        c_odd+=1
    if i>0:
        c_pos+=1
    elif i<0:
        c_neg+=1
    else:
        c_zer0+=1

print(f"The given list is : {li}")
print(f"The counts:\nEven : {c_even} \nOdd : {c_odd} \nPositive : {c_pos} \nNegative : {c_neg} \nZero : {c_zer0}")


# Seperate a list of integers into two list: even numbers and odd numbers.

li=[12,2,3,4,43,43,23,232,1]
li_even=[]
li_odd=[]

for i in  li:
    if i % 2==0:
        li_even.append(i)
    else:
        li_odd.append(i)

print(f"Even : {li_even} \nOdd : {li_odd}")

# Given a list, create a new list containing the squares of all its elements using a list comphrehension. 

li=[12,12.2,21.2,21.2,212.2,21212,121,-212,21,0,2121,3323.23,32.2]

new_list=[i**2 for i in li]

print(new_list)

# Create a list of numbers from 1 to 100 divisible by both 3 and 5.

li=[i for i in range(1,101) if i%3==0 and i%5==0]
print(li)