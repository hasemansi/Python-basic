dict1={
    'Name':'Mansi',
    'Age':21,
    'Class':'MCS-II'
}
print(dict1)
print(type(dict1))

# does it stores the values by index or not 
# print(dict1[0]) # no

# retrive
print(dict1['Name'])
print(dict1['Class'])

#update
dict1['Age']=22
print(dict1)

#add
dict1['Salary']=50000
print(dict1)

#delete
dict1.pop('Class')
print(dict1)

# allows duplicate keys ----> No ----> it update the value of last key with the previous

vehicle = {
    "color":"red",
    "type":"sedane",
    "type":"SUV"
}
# {'color': 'red', 'type': 'SUV'}
print(vehicle)

#loop
for key in dict1:
    print(key,dict1[key])

# in keyword
print('Name' in dict1)

vehicle = {
    "color":"red",
    "type":"sedane",
    "passing":"pune",
    "color":"blue"

}

for key in vehicle:
    print(key) # returns all keys
    print(vehicle[key]) # return all values

student = {
    "firstName":"alice",
    "lastName":"patil",
    "age":12,
    "rollNo":36
}   

print(student['firstName'])
print(student.get('age'))

# print('hello')
# print(student['language'])  # execution halt 
# print('bye')

print('hello')
print(student.get('language'))   # it returns none
print('bye')

student.clear()
print(student) # return empty dictionary after clear()

student = {
    "firstName":"shyam",
    "lastName":"rao",
    "age":12,
    "rollNo":36
}

student.update({'language':'English','Skill':'Python'})
print(student)
print(len(student))

student.pop('rollNo') # pass the key 
print(student)

student.popitem() # delete the last key value pair
print(student)

for x in student.keys():  # returns all keys
    print(x)

for x in student.values():  # return all the values
    print(x)

for x in student.items(): # returns all the key - value pairs
    print(x)

# if property exist will return its value , else will set the default value
print(student.setdefault('age',22))
# if property does not exist ?
print(student.setdefault('city',"pune"))
print(student)

# create a dictionary with keys
print(dict.fromkeys(['key1','key2','key3']))  # value set to none for all keys


# copy the dictionary
studA=student
print(studA)

studA.update({'city':'mumbai'})
print(studA)  # {'firstName': 'shyam', 'lastName': 'rao', 'age': 12, 'language': 'English', 'city': 'mumbai'}
print(student) # {'firstName': 'shyam', 'lastName': 'rao', 'age': 12, 'language': 'English', 'city': 'mumbai'}

studB=student.copy()
print(studB)
studB.update({'city':'pune'})
print(studB) # {'firstName': 'shyam', 'lastName': 'rao', 'age': 12, 'language': 'English', 'city': 'pune'}
print(student) # {'firstName': 'shyam', 'lastName': 'rao', 'age': 12, 'language': 'English', 'city': 'mumbai'}