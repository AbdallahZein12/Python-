from PIL import Image
import random,time,sys, os



def main():
    global par1
    global par2
    
    
        
    

    os.system('cls')
    print("\033[?25l")

    with Image.open('logo.png') as im:
        im = im.convert('L')
        im = im.resize((210,20))
        chars = '.:-=+*#%@'
        for y in range(im.size[1]):
            time.sleep(0.05)
            for x in range(im.size[0]):
                gray = im.getpixel((x,y))
                char = chars[gray * len(chars) // 355]
                
                print(char,end='')
            print()


    print("\033[?25h",end='')
    print()
    print()

    colors_list = ["\033[30m","\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"]

    while True:
        
        string = input("input your word:  ")
        if string.isalpha:
            print("\033[?25l")
            break
        else:
            print()
            print("\033[31m","Error! Please try again","\033[0m",sep='')
            print()
    os.system('cls')





    par1 = 0
    par2 = -1

    def string_checker(string,i):
        global par1
        global par2 

        par1+=2
        par2+=2
        
        if str(string[i]) != str(string[(i+1) * -1]):
            print()
            print()
            print("NOT A PALINDROME")
            print( string[i] + " is not " + string[(i+1)*-1], ":(") 
            print()
            
            
        else:
            try:
                if len(string) % 2 == 0 and len(string)-i == len(string) // 2:
                    result = random.choice(colors_list) + string[i]
                    time.sleep(1)
                    print(result)
                    print()
                    print()
                    print("ITS A PALINDROME!!!")
                    print()
                   
                    return
                elif len(string) % 2 != 0 and len(string)-i-1 == len(string) //2:
                    result = random.choice(colors_list) + string[i]
                    time.sleep(1)
                    print(result)
                    print()
                    print()
                    print("ITS A PALINDROME!!!")
                    print()
                   
                    return
                else:
                    result =  random.choice(colors_list) + string[i] + (" " * (len(string)-par1)) + random.choice(colors_list) + string[-i-1] + "\033[{}D".format(len(string)-par2)
                print(result,end='',sep="")
            
                time.sleep(1)
                sys.stdout.flush()
                
                result + string_checker(string, i+1)
                
            except:
                return

    
        
                

            
    string_checker(string, 0)
    print("\033[?25h")
    while True:
        try_again = input("Try again?(y/n)> ")
        if try_again.lower().strip() == "n":
            os.system('cls')
            print("\033[?25l")
            print("Thank you for playing!")
            time.sleep(2)
            quit()
        elif try_again.lower().strip() == "y":
            main()
        else:
            print()
            print("\033[31m","Error! Please try again","\033[0m",sep="")
            print()
            continue
    
    

main()