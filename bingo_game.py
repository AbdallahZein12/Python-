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

def program():
  def title(string):
      for i in range(len(string)):
          print(f"{colors(generator(0,3))}{string[i]}{colors('reset')}",end='')
          sys.stdout.flush()
          time.sleep(0.1)
  print("\033[?25l",end='')
  title("Bingooo!!")
  print("\033[?25h")
  
  
  
  
  
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
                
      def prettyprint():
      
        print(f"""
        {list1[0][0]}   |      {list1[0][1]}     |   {list1[0][2]}
        --------------------------
        {list1[1][0]}   |   "BINGO"  |   {list1[1][1]}
        --------------------------
        {list1[2][0]}   |      {list1[2][1]}     |   {list1[2][2]}""")
      prettyprint()
      def game():
        while True:
          try:
            print()
            print()
            number = input("Next Number: ")
            int(number)
            break
          except:
            print()
            print(f"{colors('red')}Error, Try again!{colors('reset')}")
            continue
        
      
        for i in range(len(list1)):
          for j in range(len(list1[i])):
            if int(number) == list1[i][j]:
              list1[i][j] = 'X'
        
      
        if list1[0][0] and list1[0][1] and list1[0][2] == 'X':
          if list1[1][0] and list1[1][1] == 'X':
            if list1[2][0] and list1[2][1] and list1[2][2] == 'X':
              os.system('clear')
              prettyprint()
              print("\033[?25l")
              title('YOU WIN!!')
              print("\033[?25h")
              print()
              while True:
                print(f"{colors('yellow')}")
              
                again = input("Would you like to play again(y/n): ")
                print(f"{colors('reset')}")
                if again.lower().strip() == 'y':
                  os.system('clear')
                  program()
                elif again.lower().strip() == 'n':
                  print()
                  print(f"{colors('blue')}Thank you for playing!!!{colors('reset')}")
                  time.sleep(2)
                  exit()
                else:
                  print(f"{colors('red')}Oops! I didn't get that. Please try again!{colors('reset')}")
                  continue
      
                  
              
            else:
              os.system('clear')
              prettyprint()
              game()
          else:
            os.system('clear')
            prettyprint()
            game()
        else:
          os.system('clear')
          prettyprint()
          game()
          
          
            
        
      # for i in list1:
      #   for j in i:
      #     if j == number:  
      #       j = 'X'
        
      
      game()
              #   for y in x:
              #     if y == 'X':
              #       print("You won!")
          
            
          
          
        
    
  
  
  bingo()

program()