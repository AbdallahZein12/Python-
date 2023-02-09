import traceback, time, os, sys, random
from getpass import getpass



while True:
    try:
        f = open("orders.txt","r")
        orders = eval(f.read())
        f.close()
        break
    except:
        orders = []
        break


def colors(col):
    if col.lower().strip() == 'red':
        return "\033[31m"
    elif col.lower().strip() == 'green':
        return "\033[32m"
    elif col.lower().strip() == 'black':
        return "\033[30m"
    elif col.lower().strip() == 'yellow':
        return "\033[33m"
    elif col.lower().strip() == 'blue':
        return "\033[34m"
    elif col.lower().strip() == 'magenta':
        return "\033[35m"
    elif col.lower().strip() == 'cyan':
        return "\033[36m"
    else: 
        return "\033[0m"
colors_list = ['red','green','black','yellow','blue','magenta','cyan']

def space(pos):
    space_ = ""
    print(f"{space_ : {pos}}",end='')


def color_printer(string):
    for i in string:
        print(colors(random.choice(colors_list)),i,end='',sep='')
        sys.stdout.flush()
        time.sleep(0.05)

def pretty_printer():
    space(">3")
    print("Name",end='')
    space(">6")
    print("Number Of Pizzas",end='')
    space(">9")
    print("Size Of Pizzas",end='')
    space(">12")
    print("Price")
    space(">3")
    print("------------------------------------------------------------------")
    print()
    print()
    c = 0
    for row in orders:
        space(">3")
        print(c,'-',row[0],"   |         ",end='')
        print(row[1],"           |      ",end='')
        print(row[2],"           |      ",end='')
        print(row[3])
        print()
        c+=1
    f = open("orders.txt",'w')
    f.write(str(orders))
    f.close()


def adder():
    global home 
    pretty_printer()
    print()
    print()
    row = ["","","",""]
    order_name = input("Name please> ")
    row[0] = order_name.title()
    orders.append(row)
    os.system('cls')
    pretty_printer()
    print()
    print()
    while True:
        num_pizzas = input("How many pizzas are you ordering> ")
        try:
            num_pizzas_ = int(num_pizzas)
            total_pizzas = num_pizzas_
            print()
        except:
            print()
            print(colors('red'),"Error! Please try again", colors('yellow'),sep='')
            print()
            continue
        if num_pizzas_ >= 100:
            print()
            print(colors('red'),"We don't have that many :(",colors('yellow'),sep='')
            print()
            continue
        else:
            row[1] = num_pizzas_
            orders.pop()
            orders.append(row)
            break
    
    while True:
        sizes_large = input("How many large ones> ")
        try:
            sizes_large_ = int(sizes_large)
        except:
            print()
            print(colors('red'),"Error! Please try again", colors('yellow'),sep='')
            print()
            continue
        if sizes_large_ > num_pizzas_:
            print()
            print(colors('red'),'Your order is less than that',colors('yellow'),sep='')
            print()
            continue
        elif sizes_large_ < num_pizzas_: 
            num_pizzas_ -= sizes_large_
            print()
            while True:
                sizes_medium = input("How many medium> ")
                try:
                    sizes_medium_ = int(sizes_medium)
                except:
                    print()
                    print(colors('red'),"Error! Please try again", colors('yellow'),sep='')
                    print()
                    continue
                if sizes_medium_ > num_pizzas_:
                    print()
                    print(colors('red'),'Your order is less than that',colors('yellow'),sep='')
                    print()
                    continue
                elif sizes_medium_ < num_pizzas_:
                    num_pizzas_ -= sizes_medium_ 
                    print()
                    while True:
                        sizes_small = input("How many small> ")
                        try:
                            sizes_small_ = int(sizes_small)
                            total__ = sizes_large_ + sizes_medium_ + sizes_small_
                        except:
                            print()
                            print(colors('red'),"Error! Please try again", colors('yellow'),sep='')
                            print()
                            continue
                        if total_pizzas != total__:
                            print()
                            print(colors('red'),"Error! Please try again", colors('yellow'),sep='')
                            print()
                            continue
                        else:
                            string1_ = f"{sizes_large_}L {sizes_medium_}M {sizes_small_}S"
                            row[2] = string1_
                            orders.pop()
                            orders.append(row)
                            price_large = 10
                            price_medium = 5
                            price_small = 3
                            price = (price_large * sizes_large_) + (price_medium * sizes_medium_) + (price_small * sizes_small_)
                            row[3] = f"{price}$"
                            orders.pop()
                            orders.append(row) 
                            os.system('cls')
                            pretty_printer() 
                            print()
                            print()
                            home_return = getpass("Press enter to go back to home")      
                            home()
                    
                else:
                    string_ = f"{sizes_large_}L {sizes_medium_}M"
                    row[2] = string_
                    orders.pop()
                    orders.append(row)
                    price_large = 10
                    price_medium = 5
                    price_small = 3
                    price = (price_large * sizes_large_) + (price_medium * sizes_medium_)
                    row[3] = f"{price}$"
                    orders.pop()
                    orders.append(row) 
                    os.system('cls')
                    pretty_printer() 
                    print() 
                    print()
                    home_return = getpass("Press enter to go back to home")
                    home()
            
        else:
            string = f"{sizes_large_}L"
            row[2] = string
            orders.pop() 
            orders.append(row)
            price_large = 10
            price_medium = 5
            price_small = 3
            price = (price_large * sizes_large_)
            row[3] = f"{price}$"
            orders.pop()
            orders.append(row) 
            os.system('cls')
            pretty_printer() 
            print()
            print()
            home_return = getpass("Press enter to go back to home")
            home()


def remover():
    global home
    pretty_printer()
    print()
    print()
    while True:
        item1 = input("What item number would you like to remove> ")
        try:
            item_1 = int(item1)
        except:
            print()
            print(colors('red'),"Error, Please try again",colors('yellow'),sep='')
            print()
            continue
        if item_1 in range(0,len(orders)):
            orders.remove(orders[item_1])
            os.system('cls')
            pretty_printer()
            print()
            print()
            home_return = getpass("Press enter to go back to home")
            home()
        else:
            print()
            print(colors('red'),"Error, Please try again",colors('yellow'),sep='')
            print()
            continue
            
    
                            
                    
                     
                    
    

        
def home():
    os.system('cls')
    print("\033[?25l",end='')
    color_printer("FNAF PIZZA")
    print()
    print()
    print()
    print("Large Pizza : 10$")
    print()
    time.sleep(0.3)
    print("Medium Pizza : 5$")
    print()
    time.sleep(0.3)
    print("Smal Pizza : 3$")
    print()
    print()
    print()
    choice1 = "1-View Orders!"
    choice2 = "2-Add Order!"
    choice3 = "3-Remove an Order!"

    print(colors('green'),end='')
    print(choice1,end='')
    sys.stdout.flush()
    time.sleep(0.3)
    space(">10")
    print(colors('yellow'),end='')
    print(choice2,end='')
    sys.stdout.flush()
    time.sleep(0.3)
    space(">15")
    print(colors("red"),end='')
    print(choice3,colors("yellow"),sep='')
    print()
    print()
    print("\033[?25h",end='')
    
    while True:
        user = input("(1/2/3)> ")
        try:
            user_ = int(user)
        except:
            print()
            print(colors('red'),"Error please try again!",colors('yellow'),sep ='')
            print()
            continue
        if user_ == 1:
            os.system('cls')
            print("\033[?25l")
            pretty_printer()
            print()
            print()
            user2 = getpass("Press enter to go back to home")
            os.system("cls")
            home()
        elif user_ == 2:
            os.system('cls')
            adder()
        elif user_ == 3:
            os.system('cls')
            remover()
        else:
            print()
            print(colors('red'),"Error Please try again",colors('yellow'),sep='')
            print()
            continue
        
        

home()






