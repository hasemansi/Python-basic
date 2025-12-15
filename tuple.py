# list -------------> mutable , stores the value by imdex
list=[0,1,2,3,4,5]
print(type(list))
print(list)

# dictionary -------------> mutable, store the values in key value pair
dict1={
    'name':'Alias',
    'age':25
}
print(dict1)
print(type(dict1))

# tuple ---------->immutable,stores the value by index
a=11,
print(type(a))
print(a)
print(a[0])
b=(10,20,30,40,50)
print(b)
#b[30]=70  # error
# print(b)

#allows duplicate value or not       -------> yes
b=(10,20,30,40,50,20)
print(b)  
c=11,22
print(c)

fruits=('apple','banana','cherry','orange','mango')
# value present in tuple
print('apple' in fruits)

print(len(fruits))

num=(11,44,73,37,59,30,58)
print(max(num))
print(min(num))

# unpacking

number=(11,22,33)
a,b,c=number
print(a)
print(b)
print(c)

print("******************")
# for -range
for x in range(len(num)):
    print(num[x])

print("*******************")
# for each loop
for x in num:
    print(x)

#while loop
i=0
while(i<len(num)):
    print(num[i])
    i=i+1

#count
n=(10,20,30,20,50)
print(n.count(20))

#index
fruits=('apple','banana','cherry','orange','mango')
print(fruits.index('banana'))
