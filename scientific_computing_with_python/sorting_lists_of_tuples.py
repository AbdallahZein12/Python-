d = {'a':10, 'b':1, 'c':22}
print(d.items())
print(sorted(d.items()))

for k,v in sorted(d.items()):
    print(k,v)
    
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
    
print(tmp)
# [(10,'a'),(22,'c'),(1,'b')]
tmp = sorted(tmp, reverse=True)
print(tmp)
# [(22,'c'),(10,'a'),(1,'b')]

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
    
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key,val)
    
c = {'a':10,'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))
