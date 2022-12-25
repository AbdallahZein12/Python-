import os, time
counter = 6
def start():
  os.system('clear')
  time.sleep(0.5)
  print("\033[34m","Hangman! 🪂","\033[0m")
  time.sleep(0.2)
  print("\033[33m")
  word = input("Input your word> ").strip().lower()
  print("\033[0m")
  os.system('clear')
  list = []
  
  def counter1():
    global counter 
    counter -= 1  
    return counter

  def checker():  
    for index in range(len(word)):
      if word[index] in list:
        print(word[index],end="")
      else:
        print("_",end='')
    

  
  
    
    


  def program():
    print("\033[33m",end='')
    ask1 = input("Letter> ").lower().strip()
    print("\033[0m")
    if ask1.lower().strip() in list:
      print()
      print("\033[31m","You already picked this!","\033[0m")
      print()
      checker()
      print()
      print()
      program()
      
    elif ask1.lower().strip() not in list: 
        if ask1 in word:
          list.append(ask1)
          checker()
          if set(list) == set(word):
            print()
            print()
            print("\033[32m",word,sep='')
            print()
            print("CORRECT!!!\nYou won with",counter,"tries left!")
            print("\033[0m")
            while True:
              print("\033[33m",end="")
              again = input("Would you like to play again? (y/n)> ")
              print("\033[0m",end="")
              if again.lower().strip() == "y":
                counter == 6
                start()
              elif again.lower().strip() == "n":
                print()
                print("\033[34m","Thanks for playing!",sep='')
                time.sleep(0.5)
                exit()
              else: 
                print()
                print("\033[31m","I didn't catch that! Please try again","\033[0m")
                print()
                continue
            
          print()
          print()
          program()

        else: 
          print("\033[31m","WRONG!!","\033[0m",sep="")
          print()
          checker()
          print()
          print()
          if counter == 1:
            print("\033[31m",f"You lost!, The answer was >> [{word}]","\033[0m")
            while True:
              print("\033[33m")
              again = input("Would you like to play again? (y/n)> ")
              print("\033[0m",end='')
              if again.lower().strip() == "y":
                counter == 6
                start()
              elif again.lower().strip() == "n":
                print()
                print("\033[34m","Thanks for playing!","\033[0m")
                time.sleep(0.5)
                exit()
              else: 
                print()
                print("\033[31m","I didn't catch that! Please try again","\033[0m")
                print()
                continue
            
          else:
            print(counter1(),"Attempts left")
            print()
        
        
          program()
        
    

  program()
start()
