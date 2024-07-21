import sys
print("hello")
print(sys.version)
#if 7 > 5:
 #   print("yse")
x=10
y=30
z=x+y
print(z)

print(type(x))

print(str(x))
print(float(x))

firstName = "Chinedu"
lastName = "Okorie"
fullName = firstName + lastName
print(fullName)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

myName="Chinedu Okorie"
def sayMyName(name):
    if name=="Chinedu":
       print(name)
    else:
        print("Not Chinedu")
    
    
sayMyName("chinedu")

#casting
x= str(10)
print(x)
y=40
print(y)

print (float(5))
import random
print(random.randrange(1,10))

if "chinedu" in "chinedu is a man":
    print("true")
else:
    print("false")
    
age=20
myName =f"Chinedu sunday i am  {age} years old"
print(myName)

print("ChineDu okorie".swapcase())
