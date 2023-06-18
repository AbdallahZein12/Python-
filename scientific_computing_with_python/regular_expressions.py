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