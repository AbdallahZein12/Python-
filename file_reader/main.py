import time,os, random,sys
os.system('cls') 
print('\033[?25l',end='')
def colors(i):
    if i == 'red' or i == 0:
        return '\033[31m'
    elif i == 'green' or i == 1:
        return '\033[32m'
    elif i == 'yellow' or i == 2:
        return '\033[33m'
    elif i == 'blue' or i == 3:
        return '\033[34m'
    elif i == 'magenta' or i == 4:
        return '\033[35m'
    else:
        return '\033[0m'

colors_list = ['red','green','yellow','blue','magenta']
def random_col():
    return random.randint(0,len(colors_list)-1)
    

def billboard(string,timer):
    counter_ = 0
    while counter_ != timer:
      for i in string:
        print(colors(random_col()), i, end='')
      print()
      sys.stdout.write("\033[F")
      counter_ += 1
f = open('high.score.txt','r')


list_ = {

}
list  = []
content = f.readlines()
for i in content:
    for char in i:
        if char.isdigit():
            index = i.index(':')
            name = i[:index].strip()
            num = int(i[index+1:])
            list_[name] = num
            break

max_value = max(list_.values())
max_key = [k for k, v in list_.items() if v == max_value]
              
print(f"{colors('yellow')}⭐Current Leader⭐")
print()
billboard('Evaluating!',10000)
print()
print()
time.sleep(0.5)
print(f"{colors('yellow')}Current leader 👑")
print()
print()
time.sleep(0.5)
if len(max_key) > 1:
    print('DRAW')
    print()
    for i in max_key:
        print(i,'   ',end='')
        sys.stdout.flush()
    time.sleep(0.5)
    print(max_value)
else:
    print(max_key[0],end='')    
    sys.stdout.flush()
    time.sleep(0.5)
    print('       ',max_value)

f.close()
