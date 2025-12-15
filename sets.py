setA={11,22,33,44}
setB={33,44,55,66,77,88}

print(type(setA))
print(setA)
print(setB)

# stes does not support duplicate values
setC={11,22,33,44,11}
print(setC)  #op: {33, 11, 44, 22}

# set stores the value by index-----NO
# print(setC[0])

# sets are immuatble

# in opeartor
print(11 in setC)
print(555 in setC)

# len 
print(len(setC))

# min and max
set1={12,54,72,59,25,59,37}
print(min(set1))
print(max(set1))

# methods
#1 add()
set1.add(89)
print(set1)

# 2.clear ()
setC.clear()
print(setC)

# 3.pop()
print(set1.pop())
print(set1)

# 4.remove(value)
set1.remove(12)
print(set1)

# 5.copy
set2=set1.copy()
print(set2)
set2.remove(54)
print(set1)
print(set2)


print("*************************")

# methods with 2 sets
# 1.intersection--->Return a new set with elements common to the set and all others
set1={11,22,33,44}
set2={33,44,55,66}

print(set1.intersection(set2))

#intersection_update ----> Update the set, keeping only elements found in it and all others.
set1={11,22,33,44}
set2={33,44,55,66}
set1.intersection_update(set2)
print(set1)

#difference------> Return a new set with elements in the set that are not in the others
set1={11,22,33,44}
set2={33,44,55,66}

print(set1.difference(set2)) #op:{11,12}
print(set2.difference(set1)) #op:{66, 55}

#difference_update------> Update the set, removing elements found in others.
set1.difference_update(set2)
print(set1) #op - {22, 11}

# symmetric_difference--------> Return a new set with elements in either the set or other but not both.
set1={11,22,33,44}
set2={33,44,55,66}
print(set1.symmetric_difference(set2))  # op {66, 11, 22, 55}

# symmetric_difference_update

set1.symmetric_difference_update(set2)
print(set1)  # op {66, 11, 22, 55}

# disjoint---------> Return True if two sets have a null intersection.
print(set1.isdisjoint(set2))  # false
set3={1,2,3}
set4={5,6,7}
print(set3.isdisjoint(set4))  # true

# issubset--->Report whether another set contains this set.
#superset---->Report whether this set contains another set
set3={1,2,3}
set4={5,6,1,7,2,3,9}

print(set3.issubset(set4)) #true
print(set3.issuperset(set4)) #false
print(set4.issubset(set3))  # false
print(set4.issuperset(set3))  # true

#union -----> Return a new set with elements from the set and all others.
print(set3.union(set4))
# {1, 2, 3, 5, 6, 7, 9}

# discard()
# emove an element from a set if it is a member.

# Unlike set.remove(), the discard() method does not raise
# an exception when an element is missing from the set
set3.discard(3)
print(set3)

set3.discard(9)
print(set3) # it returns nothing and does not raise any error