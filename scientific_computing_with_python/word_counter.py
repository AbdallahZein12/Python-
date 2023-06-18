name = input("Input your file name: ")
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
        
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
    
    
d = {'a':10,'b':1, 'c':22}
c = d.items()
print(c)
c = sorted(d.items())
print(c)



c = {'a':10,'b':1,'c':22}
tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)


fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    
lst = list()
for key, val in counts.items():7
    newtup = (val, key)7
    lst.append(newtup)
    
lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)
    
    
c = {'a':10,'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()]))

print("\033[32m")