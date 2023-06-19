# ^   Matches the beginning of a line
# $   Mathces the end of the line
# .   Mathces any character
# \s  Matches whitespace
# \S  Matches any non-whitespace character
# *   Repeats a character zero or more times
# *?  Repeats a character zero or more times (non-greedy)
# +   Repeats a character one or more times
# +?  Repeats a character one or more times (non-greedy)
# [aeiou] Matches a single character in the listed set
# [^XYZ]  Matches a single character not in the listed set
# [a-z0-9]    The set of characters can include a range
# (   indicates where string extraction is to start
# )   indicates where string extraction is to end

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
        
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)


hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
        
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
        
        
x = "My 2 favorite numbers are 19 and 42"
y = re.findall('[0-9]+',x)
print(y)


print(re.findall('[AEIOU]+',x))

x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)
x = 'From: Using the : character'
y = re.findall('^F.+?:',x)
print(y)

print(re.findall('\S+@\S+',x))

print(re.findall('^From (\S+@\S+)',x))

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:',max(numlist))


