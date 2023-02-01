import sys,time,os,random


def colors(col):
    if col.lower().strip() == 'red':
        return '\033[31m'
    elif col.lower().strip() == 'green':
        return '\033[32m'
    elif col.lower().strip() == 'yellow':
        return '\033[33m'
    elif col.lower().strip() == 'blue':
        return '\033[34m'
    elif col.lower().strip() == 'magenta':
        return '\033[35m'
    elif col.lower().strip() == 'cyan':
        return '\033[36m'
    elif col.lower().strip() == 'white':
        return '\033[37m'
    else:
        return '\033[0m'

counter = 0



def title_checker():
    w = open('my.ideas.txt','a+')
    r =  open('my.ideas.txt','r')
    lines = r.readlines()
    try:
        if lines[0] != 'Your ideas!\n':
            lines[0] = 'Your ideas!\n\n'
            r.close()
            r = open('my.ideas.txt','w')
            r.writelines(lines)
            r.close()
            w.close()       
        else:
            r.close()   
            w.close()
    except:
        counter = 0
        w.write('Your ideas!\n\n')
        w.close()



def rand_col():
    colors_list = ['red','green','yellow','blue','magenta','cyan','white']
    num = random.randint(0,len(colors_list)-1)
    return colors(colors_list[num])



def string_printer(str):
    for i in str: 
        print(rand_col(),i,end='',sep = '')
        sys.stdout.flush()
        time.sleep(0.1)
        

def space(pos):
  space_ = ''
  print(f"{space_:{pos}}", end='')


def adder():
    ideas = []
    # global counter
    os.system('cls')
    r = open('my.ideas.txt','r')
    lines = r.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i][3:]

    ideas = lines[2:]
    r.close()

    while True:
        print(colors('yellow'),end='')
        idea = input('Input your random idea> ')
        # counter+=1 
        idea_ = idea.title().strip()
        if idea_ in ideas:
            print()
            print(colors('red'),'Looks like you already added this! Please try again',colors('yellow'),sep='')
            print()
            continue
        else:
            ideas.append(idea_)
            break

    w = open('my.ideas.txt','a')
    string = f"{len(ideas)}- {idea_}"
    w.write(f"{string}\n")
    w.close()
    
    os.system('cls')
    print('Adding')
    cc = 10
    while True: 
        string_printer('...')
        print()
        sys.stdout.write("\033[F")
        if cc == 0:
            break
        else:
            cc -= 1

    os.system('cls')
    print(colors('green'),'Successfully added!',colors('yellow'))
    print()

    while True:
        user__ = input('Add more or return to menu(a/m)> ')
        if user__.lower().strip() == 'a':
            adder()
        elif user__.lower().strip() == 'm':
            global main
            main()
        else:
            print()
            print(colors('red'),'Error, Please try again!',colors('yellow'))
            print()
            continue
             
    
def random_generator():
    global main
    os.system('cls')
    r = open('my.ideas.txt','r')
    lines = r.readlines()
    ideas = lines[2:]
    for i in range(len(ideas)):
        ideas[i] = ideas[i].strip()
        ideas[i] = ideas[i][3:]
    r.close()

    if len(ideas) < 1:
        print('Looks like your list is empty!')
        print()
        print('Returning to main menu...')
        time.sleep(5)
        main()

    print('Generating!')
    cc = 5
    while True:
        string_printer('...')
        print()
        sys.stdout.write("\033[F")
        if cc == 0:
            break
        else:
            cc -= 1

    idea_chosen = random.randint(0,len(ideas)-1)
    os.system('cls')

    print(colors('green'),ideas[idea_chosen],colors('yellow'))
    print()

    while True:
        user__ = input('Generate again or return to menu(r/m)> ')
        if user__.lower().strip() == 'r':
            random_generator()
        elif user__.lower().strip() == 'm':
            
            main()
        else:
            print()
            print(colors('red'),'Error, Please try again!',colors('yellow'))
            print()
            continue

    


def previewer():
    os.system('cls')
    r = open('my.ideas.txt','r')
    lines = r.readlines()
    ideas = lines[2:]
    r.close()
    for i in range(len(ideas)):
        ideas[i] = ideas[i].strip()
    
    for i in ideas:
        print(i,'\n')

    while True:
        user__ = input('Return to menu(m)> ')
        if user__.lower().strip() == 'm':
            global main
            main()
        else:
            print()
            print(colors('red'),'Error, Please try again!',colors('yellow'))
            print()

def idea_clearer():
    os.system('cls')
    f = open("my.ideas.txt","w")
    f.close()
    print(colors('green'),'Cleared successfully 💣',colors('yellow'))
    print()
    while True:
        user__ = input('Return to menu(m)> ')
        if user__.lower().strip() == 'm':
            global main
            main()
        else:
            print()
            print(colors('red'),'Error, Please try again!',colors('yellow'))
            print()
        


def main():
    title_checker()
    os.system('cls')
    print('\033[?25l',end='')
    string_printer('⭐Idea Storage⭐')
    print()
    print()
    space('>25')
    print(colors('yellow'),'Options')
    print()
    print()
    time.sleep(0.5)
    print(colors('blue'),'a - Add an idea!',end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(colors('green'),"                        r - See a random idea!")
    print()
    time.sleep(0.5)
    print(colors('cyan'),'p - Preview your ideas!',end='')
    sys.stdout.flush()
    time.sleep(0.5)
    print(colors('magenta'),"                        c - Clear list!")
    print()
    print()
    time.sleep(0.5)
    while True:
        print(colors('yellow'),end='')
        user = input('a/r/p/c> ')
        if user.lower().strip() == 'a':
            adder()
        elif user.lower().strip() == 'r':
            random_generator()
        elif user.lower().strip() == 'p':
            previewer()
        elif user.lower().strip() == 'c':
            idea_clearer()
        else:
            print()
            print(colors('red'),'Error! Please try again',colors('yellow'))
            print()
            continue

    

main()
