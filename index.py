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

print(bool(""))

print (2<5 or 5<2)

thislist = ["apple", "banana", "cherry"]
print(thislist[-2])

print(len(thislist))

for item in thislist:
    print(item)
    
    
[(print(x)) for x in thislist] #shorthand for looping


mums =[1,2,3,4,]
i=0;
while i < len(mums):
    print(mums[i]+1)
    i=i+1
   
evens=[] 
def filterEven(numbers):
    for n in numbers:
        if n%2==0:
           evens.append(n)
 
filterEven([1,3,5,6,7,8,9,10,]) 
print(evens) 

list1=[3,6,1,2,7,8,0]
list1.sort()
print(list1)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)