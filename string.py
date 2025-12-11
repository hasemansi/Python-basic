a='Mansi'
print(a)
print(type(a))

b="""
    Hello i am learning python
    welcome
"""
print(b)

c='''
    Hello i am learning python
    welcome
 '''
print(c)

print(type(b))
print(type(c))

# striing concat
a='helo'
b='welcome'
print(a+b)

fname='shyam'
lname='patil'
print(f"my firstname is {fname} and lastname is {lname}")

# string methods
print('hello'.upper())
print('hello'.lower())
print('hello'.capitalize()) 

str="I am learning python"
print(str.capitalize())  # first letter is in capital in a string
# I am learning python
print(str.title()) # Return a version of the string where each word is titlecased.
# I Am Learning Python


# count
print(str.count('a'))
str1='Alias'
print(str1.startswith('A')) # T 
print(str1.startswith('a')) # F
print(str1.endswith('s')) # T
print(str1.endswith('as')) # T

print(str.find('am')) # Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end]

# format
text="My first name is {} and lastname is {}".format("shyam","rao")
print(text)
text1="My firstname is {fname} and lastname is {lname}".format(fname="amit",lname='patil')
print(text1)

fn="priya"
ln='patil'
text=f"my firstname is {fn} and lastname is {ln}"
print(text)

# access with index or not
city="mumbai"
print(city[1])  # yes

# mutable or immutable
# city[1]='g'  # immutable
# print(city)

# checked methods

#isalpha
print('siya'.isalpha()) # T
print('siya'.isalnum()) # T
print("1a".isalnum()) # T
print("1a".isalpha()) # F
print('2'.isalnum()) # T
print('12s#'.isalnum()) # F
print("hello".islower()) #T
print("Hello".lower()) #F
print("HELLO".isupper()) #T
print("Hello".isupper()) #F

# isSpace()
print(" ".isspace()) #T
print(". ".isspace()) #F

# join()
info=['abc','xyz','25']
print('@'.join(info)) #abc@xyz@25

#split()
mail='abc@rao@1384657'
print(mail.split('@')) #[ 'abc', 'rao', '1384657']

text='password'
print(text.rjust(10,'.')) #..password
print(text.ljust(10,'.')) # password..
print(text.center(10,'.')) # .password.

fruits= '    apple    '
print(fruits.rstrip()) # remove right side space
print(fruits.lstrip()) # remove left side space
print(fruits.strip()) # remove all left and right space

# removeprefix()
print(text.removeprefix('pas'))
#removesuffix()
print(text.removesuffix('rd'))

#replace
str2='I am learning python'
print(str2.replace('python','javascript'))

#swapcase()
print('python'.swapcase()) # PYTHON

#zfill
print('675'.zfill(5)) #00675

#partition()
email='abc2004@gmail.com'
print(email.partition('@'))
# ('abc2004', '@', 'gmail.com')