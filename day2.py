# operators
# arithematic operator + - /  % 
a=5
b=10
print(a+b)
print(a-b)
print(a/b)
print(a%b)

a=17
b=15
print(a+b)
print(a-b)
print(a/b)
print(a%b)

# function in python 
#A function in Python is a block of code that performs a specific task and can be reused whenever needed.
#It is defined using the keyword def.

def Calculator(a,b):
    print(a+b)
    print(a-b)
    print(a/b)
    print(a%b)

Calculator(10,5)
Calculator(17,14)
Calculator(9,41)

# loops in python
# while loop
#A while loop in Python is used to repeat a block of code as long as a given condition is true.
#When the condition becomes false, the loop stops.

#syntax
# while condition:
    # code block to execute

#program 1 (print 1 to 3)
i=1
while(i<=3):
    print(i)
    i+=1

#program 2 (print 1 to 5)
i1=1
while(i1<=5):
    print(i1)
    i1+=1

#program 3(print hello 5 times)
i2=1
while(i2<=3):
    print("Hello..!")
    i2+=1

# print 5 to 1
b=5
while(b>=1):
    print(b)
    b=b-1

# table of 2 
t1=2
while(t1<=20):
    print(t1)
    t1=t1+2

# table of 3 in reverse 
t2=30
while(t2>=3):
    print(t2)
    t2=t2-3

# table of 5 in reverse
t3=50
while(t3>=5):
    print(t3)
    t3=t3-5

# break statement with for loop
for x in range(1,6):
    if(x==3):
        break
    print(x)

for x in range(1,6):
    print(x)
    if(x==3):
        break


# break statement with while loop
q1=1
while(q1<=5):
    if(q1==3):
        break
    print(q1)
    q1=q1+1

q1=1
while(q1<=5):
    print(q1)
    if(q1==3):
        break
    q1=q1+1
    
#continue with while loop
q1=1
while(q1<=5):
    if(q1==3):
        q1=q1+1
        continue
    print(q1)
    q1=q1+1
