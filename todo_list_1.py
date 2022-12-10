import os, time

def col(color):
  if color == "red":
    return("\033[31m")
  elif color == "blue":
    return("\033[34m")
  elif color == "green":
    return("\033[32m")
  elif color == "yellow":
    return("\033[33m")
  else:
    return("\033[0m")

view = (f"{col('yellow')}View")
add = (f"{col('green')}Add")
rem = (f"{col('red')}Remove")
list = []

def home():
  
  print("\033[?25l", end='')
  print(f"{col('red')}={col('green')}={col('yellow')}={col('blue')}TODO List!{col('red')}={col('green')}={col('yellow')}=" , sep='')
  
  print()
  print()
  time.sleep(0.2)
  print(f"{view: >15}")
  time.sleep(0.2)
  print(f"{add: >20}")
  time.sleep(0.2)
  print(f"{rem: >28}")
  print("\033[?25h", end='')
  print()
  
  user = input(f"{col('reset')}: ") 

  if user == 'view':
    os.system('clear')
    print('\033[?25l', end='')
    print()
    for item in list:
      print(f"{col('yellow')}{item}")
    print()
  
    back = input(f"{col('reset')} Press any key to go back!")
    os.system('clear')
    home()

  elif user == 'Add' or user == 'add':
    os.system('clear')
    print('\033[?25h', end='')
    while True:
      add1 = input(f"{col('green')}What would you like to add: ")
      list.append(add1)
      os.system('clear')
      while True:
        option1 = input(f"""{col('reset')}[{add1}]{col('green')}  was successfully added to your list!\n \n add more? (y/n): """)
        if option1 != 'y' and option1 != 'Y' and option1 != 'n' and option1 != "N":
          print()
          print(f"{col('red')} I am sorry, I didn't get that. Try again! {col('green')}")
          print()
          continue
        else: 
          break
      if option1 == 'y' or option1 == 'Y':
        print()
        continue
      elif option1 == 'n' or option1 == 'N':
        os.system('clear')
        home()

  elif user == 'remove' or user == 'Remove':
    os.system('clear')
    print('\033[?25h', end='')
    while True:
      rem1 = input(f"{col('red')}What would you like to remove:")
      if rem1 in list:
        list.remove(rem1)
      else:
        print()
        print(f"{rem1} was not on the list!")
        print()
        while True:
          user3 = input("Go back to home? (y/n): ")
        
          if user3 == 'y' or user3 =="Y":
            os.system('clear')
            home()
          elif user3 == 'n' or user3 == 'N':
            break
          else:
            print()
            print("Didn't catch that!")
            print()
            continue
        print()
        continue
      
      os.system('clear')
      while True:
        option2 = input(f"{col('reset')}[{rem1}]{col('red')}  was successfully removed from your list! remove more? (y/n): ")
        if option2 != 'y' and option2 != 'Y' and option2 != 'n' and option2 != "N":
          print()
          print(f"{col('red')} I am sorry, I didn't get that. Try again! {col('red')}")
          print()
          continue
        else: 
          break
      if option2 == 'y' or option2 == 'Y':
        print()
        continue
      elif option2 == 'n' or option2 == 'N':
        os.system('clear')
        home()
  else: 
    print()
    print(f"{col('red')} Didn't catch that. Please try again!")
    time.sleep(1)
    os.system('clear')
    home()

home()