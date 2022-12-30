import time,os,random,sys

def colors(col):
    if col == "red" or col == 0:
        return "\033[31m"
    elif col == "green" or col == 1:
        return "\033[32m"
    elif col == "yellow" or col == 2:
        return "\033[33m"
    elif col == "blue" or col == 3:
        return "\033[34m"
    else:
        return "\033[0m"

def generator(min,max):
    num = random.randint(min,max)
    return num


def title(string):
    for i in range(len(string)):
        print(f"{colors(generator(0,3))}{string[i]}{colors('reset')}",end='')
        sys.stdout.flush()
        time.sleep(0.1)

title("Bingo Card Generator!!")





print()
print()

def bingo():
    list1 = [['a','b','c'],['d','e'],['f','g','h']]
    list2 = []
    e = 0
    while e < 8:
        l = generator(0,90)
        if l in list2:
            continue
        else:
            list2.append(generator(0,90))
            e += 1
            continue
    list2.sort()

    count = 0 
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            list1[i][j] = list2[count]
            if count < 7:
                count += 1
            else:
                count = 0 
    
    print(f"""
    {list1[0][0]}   |      {list1[0][1]}     |   {list1[0][2]}
    --------------------------
    {list1[1][0]}   |   "BINGO"   |   {list1[1][1]}
    --------------------------
    {list1[2][0]}   |      {list1[2][1]}     |   {list1[2][2]}""")
    
    


bingo()


    



