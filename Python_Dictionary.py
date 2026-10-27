# Day 7 of Python : Python Dictionary 

# Dictionary 

"""
= It is a collection of key values and aslo known as map or assosiative arrays.

1. Mutable 
2. Indexing has no meaning 
3. Key can't be duplicated 
4. Keys can't be mutable items (datatype)
"""

# Creating Dictionary 

# empty 
d={}
print(type(d))
print(d)

# 1D 
d1= {'name':'Dinesh', 'age':19}
print(d1)

# Mixed datatype : for key
d2={(1,2):"21",1:21}
print(d2)

# 2D 
d3={
    'name':"Dinesh",
    "age":19,
    'subject':{
        'math':100,
        'physics':21
    }
}
print(d3)

# Using dict function 
d4=dict([(1,22222222),("Hello",12)])
print(d4)


# Accessing Items 

#using key
d1= {'name':'Dinesh', 'age':19}
print(d1['name'])

print(d3)
print(d3['subject'])
print(d3['subject']['math'])



#using get

print(d1.get('age'))

# Adding key-value pair

d1['gender']='M'
print(d1)

print(d3)
d3['subject']['chem']=12
print(d3)

# Removing Key-Value pair 

# pop
d1.pop('age')
print(d1)

#popitem : last key-value
d1.popitem()
print(d1)


# del : for whole dic
print(d2)
"""
del d2
print(d2) :NameError: name 'd2' is not defined. Did you mean: 'd'?
"""

# clear : to make empty 

print(d1)
d1.clear()
print(d1)

# Editing key-value pair 

print("\n",d3)
d3["subject"]['math']=323
print(d3)

# Dictionary Operations 

# Membership : looks keys
print("subject" in d3)

#iterations

print("\n\n\n\n",d3)

for i in d3: 
    print(i,d3[i])

# Dictionary Functions 

print(len(d3))
print(sorted(d3))


print(d3.items()) # gives key -values in tuple
print(d3.keys())
print(d3.values())


# Dictionary Comprehension 

#{key : value for vars in iterable}

# print first 10 numbers and their sqaure 

di={x:x**2 for x in range(1,11)}
print(di)

# using existing dictionary
di1={key:value*2 for (key,value) in di.items()}
print(di1)


# Using zip 

a=[1,2,3,4]
b=["heloo",'32d','2f','32a']

di={a:b for a,b in zip(a,b)}
print(di)

# Using if condition 

product={'laptop':21,'mobile':212,'pc':0}

# product with zero stock 

di={x:y for x,y in product.items() if y!=0}
print(di)

