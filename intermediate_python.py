import timeit
from timeit import default_timer as timer   
from collections import Counter,namedtuple, OrderedDict, defaultdict, deque
from itertools import product, permutations,combinations, combinations_with_replacement,accumulate,groupby,count,repeat,cycle
import operator
from functools import reduce
import logging

####LISTS####
print()
print()
print("LISTS")
print()
print()
list1 = [1,3,4,-5,10,3,3]
print(list1.count(3))
if list1.count(3) > 1:
    print('y')
else:
    print('n')

new_list = sorted(list1)
print(new_list)

list2 = [0] * 15

print(list2)

list2.insert(1,5)

print(list2)

list2.pop()

print(list2)

list2.append(7)

print(list2)

list3 = new_list + list2

print(list3)

list3.reverse()

print(list3)

print(list3[::2])

copied_list = list(list3)
copied_list.append('lemon')

print(list3)
print(copied_list)

a = [1,2,3,4,5,6]
b = [i*i for i in a]

print(a)
print(b)

####TUPLES####
print()
print()
print("TUPLES")
print()
print()
mytuple = (5,)
print(type(mytuple))

mytuple2 = tuple(["banana",25,12])

print(mytuple2)

print(mytuple2[2])

for i in mytuple2:
    print(i)
    
tuple_to_list = list(mytuple2)
print(tuple_to_list)

test_tuple = (0,1,2,3,4)
i1, *i2, i3 = test_tuple
print(i1)
print(i2)
print(i3)

print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4)",number=1000000))


####DICTIONARIES####
print()
print()
print("DICSTIONARIES")
print()
print()

mydict = {"name":"Bob","age":20,"city":"New York"}

new_dict = dict(name="Mary",age=22,city="Miami")

print(mydict)
print(new_dict)

mydict.pop("name")

print(mydict)

for key,item in mydict.items():
    print(key, item)
    
mydict.update(new_dict)

####SETS####
print()
print()
print("SETS")
print()
print()
my_set = {1,2,3,4,4,3,2,1}
print(my_set)

my_set.add(5)

print(my_set)

my_set.discard(3)
print(my_set)

for i in my_set:
    print(i)
    
odds = {1,3,5,7,9}
evens = {0,2,4,6,8,10}
primes = {2,3,5,7}
odds = odds.union(evens)
print(odds)

i = odds.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7}
setB = {1,2,3,55,66,77}
setA = setA.symmetric_difference(setB)

print(setA)

setA.symmetric_difference_update(setB)
print(setA)


####STRINGS####
print()
print()
print("STRINGS")
print()
print()
my_string = "Hello World"
print(my_string[:5:2])

greeting = "Hello"
name = "Tom"

print(greeting + " " + name)

for i in greeting:
    print(i)

string = " Hello World "
string = string.strip()
print(string)

print(string.lower())
print(string.startswith('H'))
print(string.endswith("World"))

print(string.count('o'))
print(string.find("o"))

print(string.replace("World","Universe"))

my_list = string.split()
print(my_list)

my_new_string = " ".join(my_list)
print(my_new_string)


list1 = ["a"] * 1000


start = timer()
string = ""
for i in list1:
    string += i

stop = timer()

print(stop-start)


start = timer()
string1 = "".join(list1)
stop = timer()
print(stop-start)

var = "Hello"

string = "%s World" %var
print(string)

string = "{} World".format(var)
print(string)

string = f"{var} World"
print(string)

####COLLECTIONS####
print()
print()
print("COLLECTIONS")
print()
print()
a ="abccddddeeefg"
counter = Counter(a)

print(counter)

print(counter.most_common(1)[0][0])

print(list(counter.elements()))

Point = namedtuple('Point',"x,y")

pt = Point(1,-4)
print(pt)
print(pt.x,pt.y)

ordered_dict = OrderedDict()

ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)

d = defaultdict(list)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

print(d['a'])
print(d['e'])

de = deque()
de.append(1)
de.append(2)

print(de)

de.appendleft(3)
print(de)

de.popleft()
print(de)

de.extendleft([4,5,6])
print(de)

de.rotate(1)
print(de)

de.clear()
print(de)

a = [1,2]
b = [3,4]

####ITERS####
print()
print()
print("ITERS")
print()
print()
prod = product(a,b)
print(list(prod))

b = [3]

prod = product(a,b,repeat=2)

print(list(prod))

a = [1,2,3]
perm = permutations(a)
print(list(perm))

a = [1,2,5,3,4]
comb = combinations(a,2)
print(list(comb))

comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

acc = accumulate(a,func=operator.mul)
print(list(acc))

acc = accumulate(a,func=max)
print(list(acc))



a = [1,2,3,4]

group_obj = groupby(a,key=lambda x: x<3)

for key,value in group_obj:
    print(key,list(value))
    
    
for i in count(10):
    print(i)
    if i == 15:
        break
    
a = [1,2,3]
#for i in cycle(a):
    #print(i)
    
for i in repeat(1,4):
    print(i)

####LABDA####

add10 = lambda x: x+10

print(add10(5))

mult = lambda x,y: x*y

print(mult(2,3))

points2d = [(1,2),(15,1),(5,-1),(10,4)]
points2d_sorted = sorted(points2d,key= lambda x: x[0] + x[1])

print(points2d)
print(points2d_sorted)


a = [1,2,3,4,5]
b = map(lambda x: x*2,a)
print(list(b))

c = filter(lambda x: x%2==0,a)
print(list(c))

product_a = reduce(lambda x,y: x*y,a)
print(product_a)

# x = -5
# if x < 0:
#     raise Exception('X Should be positive num')

try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("All good")
finally:
    print("Cleaning up...")
    
class ValueTooHighError(Exception):
    pass

class VlaueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise VlaueTooSmallError("value is too small",x)
    
try:
    test_value(1) 
except ValueTooHighError as e:
    print(e)
except VlaueTooSmallError as e:
    print(e.message, e.value)