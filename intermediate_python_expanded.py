
print()
print("-----LISTS-----")
print()
# Lists: ordered, mutable, allows duplicate elements.
myList = ["banana","cherry","apple"]
print(myList)

myList2 = list()
print(myList2)

myList2 = [5, True, "Apple","Apple"]
print(myList2)

item = myList2[2]
print(item)

item = myList2[-2]
print(item)

for i in myList2:
    print(i)

if "banana" in myList2:
    print("yes")
else:
    print("no")
    

print(len(myList2))

myList2.append("lemon")
print(myList2)

myList2.insert(1,"blueberry")
print(myList2)

item = myList2.pop()
print(item)
print(myList2)

item = myList2.remove("Apple")
print(myList2)

myList2.reverse()
print(myList2)

myList.sort()
print(myList)

myList2.clear()
print(myList2)

new_list = sorted(myList)

myList = [0] * 5
print(myList)

myList2 = [1,2,3,4,5]

new_list = myList + myList2
print(new_list)


new_list = [1,2,3,4,5,6,7,8,9]

a = new_list[1:5]

print(a)

A = new_list[::-1]
print(A)

list_org = ["banana","cherry","apple"]

list_cpy = list_org

list_cpy.append("lemon")

print(list_org)
print(list_cpy)

list_cpy = list_org.copy()
list_cpy = list(list_org)
list_cpy = list_org[:]

list_cpy.append("hi")

print(list_cpy)
print(list_org)

myList = [1,2,3,4,5,6]
b = [i*i for i in myList]

print(myList)
print(b)


print()
print("-----LISTS-----")
print()
# Tuple: orderedm immutable, allows duplicate elements.
mytuple = ("Max", 28, "Boston")
mytuple = "Max", 28, "Boston"
mytuple = ("Max",)
mytuple = tuple(["Max", 28, "Boston"])

item = mytuple[-1]
print(item)

for i in mytuple:
    print(i)
    
if "Max" in mytuple:
    print("Yes")
else:
    print("No")
    
mytuple = ('a','p','p','l','e')

print(len(mytuple))

print(mytuple.count('p'))
    
    
print(mytuple.index('p'))


mylist = list(mytuple)
print(myList)

mytuple = tuple(myList)


a = (1,2,3,4,5,6,7,8,9,10)

b = a[2::2]
print(b)

mytuple = "Max", 28, "Boston"

name, age, city = mytuple

print(name)
print(age)
print(city)

mytuple = (0,1,2,3,4)
i1, *i2, i3 = mytuple

print(i1)
print(i2)
print(i3)

import sys
myList = [0,1,2,"hello",True]
mytuple = (0,1,2,"Hello", True)
print(sys.getsizeof(myList),"bytes")
print(sys.getsizeof(mytuple),"bytes")

import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))


print()
print("-----DICTIONARIES-----")
print()

#Dictionaries: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27,city="Boston")
print(mydict2)


value = mydict["age"]
print(value)

mydict["email"] = "max@gmail.com"

del mydict["age"]
print(mydict)

mydict.pop("email")
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict["name"])
    
try:
    print(mydict["name"])
except:
    print("Error")
    
for key in mydict2:
    print(key)
for key in mydict2.keys():
    print(key)
for value in mydict2.values():
    print(value)
for key, value in mydict2.items():
    print(key, value)
    
mydict_cpy = mydict2.copy()
mydict_cpy = dict(mydict2)

mydict = {"name":"Max", "age":28, "email":"max@xyz.com"}
mydict2 = dict(name="Mary", age=27, city="Boston")

mydict.update(mydict2)
print(mydict)


mytuple = (8, 7)
mydict = {mytuple: 15}

print(mydict)