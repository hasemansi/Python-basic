print(1)
print(2)
print(3)
print(4)
print(5)

#syntax
# for x in range(startindex,endindex(not included),stepsize):
#       statements

# range(5) ---> startIndex - 0 endIndex - 5 , stepSize- 1
# range(1,5) ---> startIndex - 1 , endIndex(5), stepSize - 1
# range(1,11,2) ---> startIndex - 1 , endIndex(11), stepsize - 2

# use range for printing the numbers from 0 to 5
for x in range(6):
    print(x)

# print(1 to 5)
for x in range(1,6):
    print(x)

# print(table of 2)
for x in range(2,21,2):
    print(x)

# another way
for x in range(1,11):
    print(x*2)

# print hello 3 times
for x in range(3):
    print("hello")

#print 5 to 1
for x in range(5,0,-1):
    print(x)

#print table of 3 in reverse
for x in range(30,1,-3):
    print(x)

print("*******************")

# break statement
for x in range(1,11):
    if(x==5):
        break  #stop the execution of a loop when a specific condition is met.
    print(x)

for x in range(2,22,2): 
    print(x) # first print then break  2 4 6
    if(x==6):
        break
    
# continue statement with for loop

for x in range(1,6): #2 #3 #4 #5
    if x == 3:
        continue
    print(x) #1 #2 #4 #5


for x in range(5,0,-1): #4 #3 #2 #1
    if x == 3:
        continue
    print(x) #5 #4 #2 #1