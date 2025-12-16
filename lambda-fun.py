# lambda  - keyword
# x,y - parameter
# return - x + y

add=lambda x,y : x+y
res=add(1,4)
print(res)

#square
sqr=lambda x : x*x
print(sqr(6))

#cube
cube=lambda a : a*a*a
print(cube(3))

# function as parameter and function  as return type

addA=lambda x ,y : x+y
print(addA)
print(addA(2,3))

#function as parameter

def addB(fn,x,y):
    e=fn(x,y)
    return e
res = addB(addA,10,3)
print(res)

# function as return type
def multiplication():
    return lambda x,y : x*y

r=multiplication()
ans = r(10,20)
print(ans)
