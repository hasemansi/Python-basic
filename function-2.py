# function
def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

cal(10,20)

# int as parameter and int as return int
def calA(x,y):
    return x+y

e=calA(12,3)
print(e)

# float as parameter and float as return type
def calB(x,y):
    return x+y
f=calB(12.6,10.36)
print(f)

#boolean as parameter boolean as return type
def canDrive(age,haveVehicle):
    if age>18 and haveVehicle:
        return True
    else:
        return False
    
f=canDrive(19,True)
print(f)

# string as parameter and string as return type
def Greet(word):
    return "Hello " + word

g=Greet('Bob')
print(g)

#list as parameter list as return type
city=["pune","mumbai","banglore","kolkata"]
def addCity(lst):
    lst.append("nagpur")
    return lst

res=addCity(city)
print(res)

# tuple as parameter and tuple as return type
num=(11,22,33,44,55)
def addTuple(t):
    tup=list(t)
    tup.append(66)
    tup=tuple(tup)
    return tup

f=addTuple(num)
print(f)

# set as a parameter and set as a return type
setA={11,22,33}
def addToSet(s):
    s.add(44)
    return s
r=addToSet(setA)
print(r)