
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