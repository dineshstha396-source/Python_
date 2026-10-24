# Day 6 of Python : Python Set

"""
# set
= A set is an unordered collection of item.

1. Unordered
2. Mutable 
3. No Duplicates 
4. Can't contain mutable data types 
"""

# Creating set

# Empty 

s={}
print(type(s)) #default is dictionary

s=set()
print(type(s))
print(s)

# 1D

s1={1,2} # Homo
print(s1)

s1={1.2,21,21,21,1,"G"} # Hetero
print(s1)

# Using type conversion 
s2=set((1,2))
print(s2)

# Duplicate not allowed 
s1={1.2,21,21,21,3,4,4,4}
print(s1)

# Accessing items : Not allowed

# Editing items : Not allowed

# Adding items 

s={1,2,3,4}

#add : one item
s.add(4)
print(s)

# update : multiple item through list
s.update([1,2,3,4,4,5,9,6,7])
print(s)

# deleting items 

s1={32,32,4}
del s1

# discard : specific item and no error
s={3,32,2,4,5,5,3,2,3}
s.discard(3)
print(s)

# remove : specific item and error
s={3,32,2,4,5,5,3,2,3}
"""s.remove(1) : KeyError: 1"""
print(s)

# pop : randomly 
s.pop()
print(s)

# clear : make the set empty 

s.clear()
print(s)

# Set Operations 

s1={1,2,3,44,4,5}
s2={4,5,6,7,8}

#Union (|)
print(s1|s2)

# intersection (&)
print(s1 & s2)

# Diff (-)
print(s1-s2)

# Symmetric diff (^)
print(s1^s2)

# membership 

print(1 in s1)

# Set function 

s={1,2,3,4,4,5,5,6}

print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))

s1={1,2,3,44,4,5}
s2={4,5,6,7,8}
s1.union(s2)

#Update

s1.update(s2) # union into s1
print(s1)



s1={1,2,3,44,4,5}
s2={4,5,6,7,8}
s1.intersection(s2)

#intersection_update

s1.intersection_update(s2) 
print(s1)


s1={1,2,3,44,4,5}
s2={4,5,6,7,8}
s1.difference(s2)

#difference_update

s1.difference_update(s2) 
print(s1)

# isdisjoint  issubset   issuperset 

s1={1,2,3,44,4,5}
s2={4,5,6,7,8}

print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))


# copy 

s2={4,5,6,7,8}
s1=s2.copy() 

print(id(s1))
print(id(s2))

# Frozenset 

""" = It is just an immutable version of a Python set object"""

fs=frozenset({1,2,3,3,3,21,21,1})
print(fs)
print(type(fs))

# Set comprehension 

# Similar to list 
s1={x for x in range(1,222222)}
print(s1)