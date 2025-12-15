# slicing
#string[start:end(not inclusive):step(1)]
#  1    2   3   4   5   6   7   8   9  
#  s    a   n   g   a   m   n   e   r
# -9 -8 -7  -6  -5  -4   -3  -2 -1

city="sangamner"
print(city[0::])
print(city[::8])
print(city[1:8])
print(city[-3:9])
print(city[-9:-1])
print(city[5::])
print(city[::2])
print(city[::3])
print(city[::-1])  # reverse the string

str="hello my name is abc"
print(str[::-1])