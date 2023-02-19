import time, os, random, sys
from getpass import getpass

colors_list_main = ['red','green','yellow']

class Color:

    @staticmethod
    def colorchng(string,col):
        colors_list_ = {
            "red":"\033[31m", "green":"\033[32m", "yellow":"\033[33m"
        }
        if col.strip().lower() in colors_list_:
            return f"{colors_list_[col]}{string}\033[0m"
        
class Billboard:
    def __init__(self,string):
        self.string = string
    
    def billboard(self,time_):
        count = 0
        while True:
            for i in self.string:
                color_chosen = random.choice(colors_list_main)
                print(Color.colorchng(i,color_chosen),end='')
                sys.stdout.flush()
                time.sleep(0.1)
            print()
            sys.stdout.write("\033[F")
            count += 1
            if count == time_:
                break
            else:
                continue 

billboard1 = Billboard("loading")

def colors(col):
    if col.lower().strip() == 'red':
        return "\033[31m"
    elif col.lower().strip() == 'green':
        return "\033[32m"
    elif col.lower().strip() == 'yellow':
        return "\033[33m"
    else:
        return "\033[0m"

def title(string):
    colors_list = ['red','green','yellow']
    for i in string:
        color_chosen = random.choice(colors_list)
        print(colors(color_chosen),i,sep='',end='')
        sys.stdout.flush()
        time.sleep(0.1)

def space(pos):
    space_ = ""
    print(f"{space_: {pos}}",end='')

def prettyprint():
    new_list = []
    print("Amount | Item")
    print()
    for i in items:
        if i in new_list:
            continue
        else:   
            amount = items.count(i)
            print(f"{amount} | {i}",end='\n')
            new_list.append(i)
        


def adder():
    global home
    os.system('cls')
    prettyprint()
    print()
    print()
    item = input("Input your item> ")
    item = item.title()
    print()

    while True:
        print(colors('yellow'),end='')
        amount = input("Input your amount> ")
        try:
            amount = int(amount)
        except ValueError:
            print()
            print(Color.colorchng("Error! Please try again","red"))
            print()
            continue
        if amount <= 0:
            print()
            print(Color.colorchng("Error! Please try again","red"))
            print()
            continue
        else:
            break

    for i in range(0,amount):
        items.append(item)
    
    with open("items.txt","w") as f:
        f.write(str(items))
    
    print()
    print()
    print("\033[?25l",end='')
    billboard2 = Billboard("Adding!")
    billboard2.billboard(3)
    os.system('cls')
    print(colors('yellow'),end='')
    prettyprint()
    print()
    time.sleep(0.5)
    print(Color.colorchng("Added Successfully!","green"))
    print()
    time.sleep(0.5)
    print(colors('yellow'),end='')
    adder_option = getpass("press any key to go back to home")
    home()

    
def viewer():
    global home
    os.system('cls')
    prettyprint()
    print()
    print(colors(""))
    adder_option = getpass("press any key to go back to home")
    home()



def remover():
    global home
    os.system('cls')
    prettyprint()
    
    if items == []:
        print("\033[?25l")
        print(colors('reset'))
        empty_list = getpass("Empty list!, Press enter to go back to home")
        home()

    print()
    while True:
        print(colors('yellow'),end='')
        item_to_remove = input("Which item would you like to remove> ")
        item_to_remove = item_to_remove.title().strip()
        if item_to_remove not in items:
            print()
            print(Color.colorchng("Error! Please try again","red"))
            print()
            continue
        elif items.count(item_to_remove) > 1:
            print()
            while True:
                print(colors('yellow'),end='') 
                amount_to_remove = input("How many would you like to remove> ")
                try:
                    amount_to_remove = int(amount_to_remove)
                except ValueError:
                    print()
                    print(Color.colorchng("Error! Please try again","red"))
                    print()
                    continue
                if amount_to_remove > items.count(item_to_remove):
                    print()
                    print(Color.colorchng("Error! Please try again","red"))
                    print()
                    continue
                elif amount_to_remove < 0:
                    print()
                    print(Color.colorchng("Error! Please try again","red"))
                    print()
                    continue
                else:
                    print()
                    print("\033[?25l")
                    billboard1.billboard(3)
                    print(colors('yellow'))
                    for i in range(0,amount_to_remove):
                        items.remove(item_to_remove)
                    
                    with open("items.txt","w") as f:
                        f.write(str(items))

                    os.system('cls')
                    prettyprint()
                    print()
                    print(colors('green'),f"Successfully removed {amount_to_remove} {item_to_remove}",colors('reset'))
                    remover_option = getpass("press any key to go back to home")
                    home()

        else:
            print()
            print("\033[?25l")
            billboard1.billboard(3)
            print(colors('yellow'))
            items.remove(item_to_remove)
                    
            with open("items.txt","w") as f:
                f.write(str(items))

            os.system('cls')
            prettyprint()
            print()
            print(colors('green'),f"Successfully removed {item_to_remove}",colors('reset'),sep='')
            print()
            remover_option = getpass("press any key to go back to home")
            home()
            
                    
                    

                    
            

            
            
    


    






def home():
    os.system("cls")
    print("\033[?25l",end='')
    title("Inventory Manager")
    print()
    print()
    print(Color.colorchng("1-Add","green"),end='')
    sys.stdout.flush() 
    time.sleep(0.3)
    space("<7")
    print(Color.colorchng("2-View","yellow"),end='')
    sys.stdout.flush()
    time.sleep(0.3)
    space("<7")
    print(Color.colorchng("3-Remove","red"),end='')
    sys.stdout.flush()
    time.sleep(0.3)
    space("<7")
    print(Color.colorchng("4-Clear","red"))


    print()
    print()
    print()
    print("\033[?25h",end='')
    print(colors('yellow'))
    while True:
        try:
            print(colors("yellow"),end='')
            home_options = int(input(">"))
        except ValueError:
            print()
            print(Color.colorchng("Error! Please try again","red"))
            print()
            continue
        if home_options == 2:
            print("\033[?25l")
            viewer()
        elif home_options == 1:
            adder()
        elif home_options == 3:
            remover()
        elif home_options == 4:
            print("\033[?25l",end='')
            os.system("cls")
            billboard1.billboard(3)
            items.clear()
            with open("items.txt","w") as f:
                f.write(str(items))
            print(colors('green'),"List cleared!",colors('reset'))
            print()
            remover_option = getpass("press any key to go back to home")
            home()
        else:
            print()
            print(Color.colorchng("Error! Please try again","red"))
            print()
            continue

        




  
    


if __name__ == '__main__':
    try:
        with open("items.txt","r") as f:
            items = eval(f.read())
    except:
        items = []
    
    home()
