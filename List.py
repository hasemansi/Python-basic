# list 
print("*********program 1*************")
names=['alia','riya','alias','bob']
print(names)
print(type(names))

numbers=[1,2,3,4,5,6,7,8]
print(numbers)
print(type(numbers))

list1=['mansi','hase',2004,22,90,0]
print(type(list1))

print(" ***********program 2*********")
# stores the value by index
print(names[0])
print(names[1])
print(names[-1])

l=len(names)
print(l)
lastindex=l-1
print(lastindex)

print("****program 3********")
# print all elements in list using for loop
cities=['sangamner','akole','nashik','pune','delhi']
print(cities)

# print cities one by one
for city in range(len(cities)):
    print(cities[city])

print("*********program 4**********")
# print elements in list using while loop
c=0
while(c<len(cities)):
    print(cities[c])
    c=c+1

print("**********List Operations**********")

print("***Append***")
flowers=['lily','jasmine','rose','lotus','sunflower']
print(flowers)
flowers.append('hibiscus')
print(flowers)

print("*****Pop*******")
flowers.pop() # removes the last element
print(flowers)

flowers.pop(0) # removes the element in particular index
print(flowers)

print("*****remove****")
flowers.remove('lotus') # Remove first occurrence of value.
print(flowers)

print("*****count******")
cnt=flowers.count('rose')
print(cnt)

print("*****clear******")
flowers.clear() # clear the whole list
print(flowers)

print("******reverse********")
cities=['sangamner','akole','nashik','pune','delhi']
cities.reverse()
print(cities)

print("********sort********")
cities.sort()
print(cities)

print("**insert element at specific index***")
cities.insert(2,'nagpur')
print(cities)

print("*******extend*********")
l1=[1,2,3,4,5,6]
l2=[7,8,9,10]
l1.extend(l2)
print(l1)

# copy
a=[10,20,30,40]
b=a  # using this it only copy the list but the memory address will remain same
print(a)
print(b)

# change in one list can also affect the other 
a[1]=70
print(a)
print(b)
# op - [10, 70, 30, 40]
# [10, 70, 30, 40]

# so we use .copy()method
c=a.copy() # this will change the memory address
# change in one can not affect the other
print(c)
c[1]=20
print(a) # [10, 70, 30, 40]
print(c) # [10, 20, 30, 40]

country = ["india","srilanka","china","cuba","india","US","Uk",'Mexico',"india"]
country.insert(2,'pakistan')
print(country)

print(len(country)) # property

#del country # delete country list

# min and max

a=[10,20,30,40]
print(min(a))
print(max(a))

# in keyword  Op in True or False
names=["sai",'alice','bob','john']
print('john' in names)

# does list stores the values by index
names=['ram','sham','alias','bob','john','rhiya','priya']
print(names[1]) # yes

# retrive all the elements of list using 
# for loop 
for n in range (len(names)):
    print(names[n])

# while loop
i=0
while(i<len(names)):
    print(names[i])
    i+=1

# for each
for x in names:
    print(x)
