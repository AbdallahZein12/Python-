
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
print("-----TUPLES-----")
print()
# Tuple: ordered immutable, allows duplicate elements.
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





print()
print("-----SETS-----")
print()

#Sets: Unordered, mutable, no duplicates


myset = {1,2,3,1,2}
print(myset)

myset = set([1,2,3])
myset = set("Hello")

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.remove(3)
print(myset)

myset.discard(3)

print(myset.pop())
print(myset)

for i in myset:
    print(i)

print(myset)
if 2 in myset:
    print("Yes")
    
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)
print(diff)

diff = setB.difference(setA)
print(diff)

diff = setA.symmetric_difference(setB)
print(diff)

diff = setB.symmetric_difference(setA)
print(diff)

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

setA.difference_update(setB)
print(setA)

setA.symmetric_difference_update(setB)
print(setA)

print(setA.issubset(setB))

print(setB.issuperset(setA))

print(setA.isdisjoint(setB))

setB = setA.copy()
setB = set(setA)

a = frozenset([1,2,3,4])


myset.clear()


print()
print("-----STRINGS-----")
print()
#Strings: ordered, immutable, text representation 

my_string = "Hello World"
print(my_string)
my_string = 'Hello World'
print(my_string)
my_string = 'I\'m a programmer'
print(my_string)
my_string = "I'm a programmer"
print(my_string)
my_string = """Hello 
World"""
print(my_string)
my_string = """Hello \
World"""
print(my_string)
my_string = "Hello World"
char = my_string[1]
print(char)
char = my_string[-1]
print(char)
substring = my_string[1:5]
print(substring)
substring = my_string[::-1]
print(substring)
greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)
for i in greeting:
    print(i)
if 'ell' in greeting:
    print("Yes")
else:
    print("No")

my_string = '   Hello World    '
my_string = my_string.strip()
print(my_string)

print(my_string.upper())
print(my_string.lower())
print(my_string.startswith('H'))
print(my_string.startswith('Hello'))
print(my_string.endswith('World'))
print(my_string.find('lo'))
print(my_string.find('pp'))
print(my_string.count('o'))
print(my_string.count('p'))
print(my_string.replace('World','Universe'))
print(my_string.replace('Worrrrld','Universe'))
my_string = "how are you doing"
my_list = my_string.split()
print(my_list)
my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)
new_string = " ".join(my_list)
print(new_string)

from timeit import default_timer as timer   

#BAD CODE BC IT CREATES A NEW STRING EVERYTIME SINCE STRINGS ARE IMMUTABLE. EXPENSIVE OPERATION
my_list = ['a'] * 100000

start = timer()
my_string = ''
for i in my_list:
    my_string += i
stop = timer()
print(stop-start)

#GOOD CODE 
start = timer()
my_string = "".join(my_list)
stop = timer()
print(stop-start)

var = "Tom"
my_string = "The variable is %s" % var
print(my_string)
var = 1
my_string = "The variable is %d" % var
print(my_string)
var = 1.122313
my_string = "The variable is %f" % var
print(my_string)
var = 1.122313
my_string = "The variable is %.2f" % var
print(my_string)
var = 1.122313
my_string = "The variable is {}".format(var)
print(my_string)
var = 1.122313
var2 = 6
my_string = "The variable is {:.2f} and {}".format(var, var2)
print(my_string)
var = 1.122313
var2 = 6
my_string = f"The variable is {var*2} and {var2}"
print(my_string)


print()
print("-----COLLECTIONS-----")
print()

# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaaaabbbbccc"

mycounter = Counter(a)
print(mycounter.keys())
print(mycounter.values())
print(mycounter.items())
print(mycounter.most_common(2))
print(mycounter.most_common(1)[0][0])
print(list(mycounter.elements()))

Point = namedtuple('Point','x,y')
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)

default_dict = defaultdict(bool)
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict['c'])

d = deque()
d.append(1)
d.append(2)
print(d)

d.appendleft(3)
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.extend([4,5,6])
print(d)

d.extendleft([4,5,6])
print(d)

d.rotate(2)
print(d)
d.rotate(-1)
print(d)


print()
print("-----ITERTOOLS-----")
print()
#itertools : product, permutations, combinations, accumulate, groupby, and infinite iterators
#Collection of tools for handling iterators (data types that can be used in a for loop)

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat
import operator
a = [1,2]
b = [3,4]
prod = product(a,b)
print(list(prod))
a = [1,2]
b = [3]
prod = product(a,b,repeat=2)
print(list(prod))


a = [1,2,3]
perm = permutations(a)
print(list(perm))
a = [1,2,3]
perm = permutations(a,2)
print(list(perm))


a = [1,2,3,4]

comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))


a = [1,2,3,4]
acc = accumulate(a)
print(list(acc))
acc = accumulate(a,func=operator.mul)
print(list(acc))
a = [1,2,5,3,4]
acc = accumulate(a,func=max)
print(list(acc))



a = [1,2,3,4]
group_obj = groupby(a,key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

people = [{'name':'Tim','age':25}, {'name':'Dan','age':25},
          {'name':'Lisa','age':27}, {'name':'Claire','age':28}]

group_obj = groupby(people, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))
    
for i in count(10):
    print(i)
    if i == 15:
        break
    
a = [1,2,3]
# for i in cycle(a):
#     print(i)
    
for i in repeat(1, 4):
    print(i)
    
print()
print("-----LAMBDA-----")
print()

# Small one line anonymous function 
# lambda arguments: expression

add10 = lambda x: x + 10
print(add10(5))

def add10_func(x):
    return x + 10

mult = lambda x,y: x * y
print(mult(2,7))

points2D = [(1,2),(15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)


points2D = [(1,2),(15,1), (5,-1), (10,4)]

def sort_by_y(x):
    return x[1]

points2D_sorted = sorted(points2D, key=lambda x: x[1])
points2D_sorted = sorted(points2D, key=sort_by_y)

print(points2D)
print(points2D_sorted)

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted)

#map(func, seq)

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(list(b))

c = [x*2 for x in a]
print(c)

#filter(func(true or false), seq)
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2==0,a)
print(list(b))
b = [x for x in a if x % 2==0]
print(b)

#reduce(func, seq)
from functools import reduce
a = [1,2,3,4]
prod_a = reduce(lambda x,y: x*y,a)
print(prod_a)

print()
print("-----EXCEPTIONS-----")
print()

# Errors and Exceptions 

# A python program terminates as soon as it encounters an error
# An error can be either a syntax error or an exception 

# a = 5 print(a)    Syntax Error!!

a = 5
# print(a))    Syntax Error!!

# a = 5 + "10"    Type Error!!

# import somemodule     Import Error!!

a = 5
# b = c      Name Error!!

# f = open('somefile.txt')     FileNotFound Error!!

a = [1,2,3]
# a.remove(4)     Value Error!!

# a[4]        Index Error!!

my_dict = {'name':'Max'}

# my_dict['age']          Key Error!!

x = 5

if x < 0:
    raise Exception('x should be positive')

assert(x>=0), 'x is not positive'

try:
    a = 5 / 0
except Exception as e:
    print('An error has occured --> ', e)

try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('Everything is fine')
finally:
    print('Cleaning up...')


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value
        

# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('Value is too high')
#     if x < 5:
#         return ValueTooSmallError('Value is too small',x)
# test_value(200)

# try:
#     test_value(200)
# except ValueTooHighError as e:
#     print(e)
# except ValueTooSmallError as e:
#     print(e.message,e.value)