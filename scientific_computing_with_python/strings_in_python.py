str = "Hello"
print('\033[0m')
str1 = "there"
bob = str + str1
print(bob)

str2 = '123'
x = int(str2) + 1
print(x)

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
    
for letter in fruit:
    print(letter)
    
count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print(count) 


s = "Monty python"

print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])

print('n' in s)
print('a' in s)

print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())

pos = fruit.find('na')
print(pos)

greet = "Hello Bob"
nstr = greet.replace('Bob','Jane')
print(nstr)
