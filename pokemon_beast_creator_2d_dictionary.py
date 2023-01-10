import time, os, sys, random

beasts = {}

colors_list = ['black', 'yellow', 'green', 'magenta', 'cyan']

def colors(col):
  if col == 'red':
    return "\033[31m"
  elif col == 'yellow':
    return "\033[33m"
  elif col == 'black':
    return "\033[30m"
  elif col == 'green':
    return '\033[32m'
  elif col == 'magenta':
    return "\033[35m"
  elif col == 'cyan':
    return "\033[36m"
  else:
    return "\033[0m"
def spaces(value):
  space = ''
  print(f"{space:{value}}",end='')

def prettyprint():
  os.system('clear')
  print('\033[?25l',end='')
  for item,value in beasts.items():
    print(item,end=">  ")
    for subitem,subvalue in value.items():
      print(subitem,':', subvalue, end=' | ')
    print()
    print()
  print()


    
  

def stringprinter(string):
  print('\033[?25l',end="")
  
  for i in string:
    print(f"{colors(random.choice(colors_list))}{i}", end='')
    sys.stdout.flush()
    time.sleep(0.1)
    

def home():
  characteristics = {'Element': None,'Special Move': None,'HP': None,'MP': None}
  count = 0
  elements = ['air','earth','fire','water']
  spaces('>15')
  stringprinter('⭐MokeBeastUltimate⭐') 
  print()
  print("\033[?25h",end='')
  print(f"{colors('cyan')}")
  color_iterator = iter(colors_list)
  beast_name = input("Input the beast Name> ").strip().title()
  for name,value in characteristics.items():
    print(f"{colors(next(color_iterator))}")
    characteristics[name] = input(f"Input the beast {name}> ").strip().title()
    count += 1
    if count == 1:
      if characteristics['Element'].strip().lower() not in elements:
        while True:
          print()
          print(f"{colors('red')}Error, Please choose an element from [Air,Earth,Water, Or Fire]{colors('reset')}")
          print(f"{colors('black')}")
          characteristics['Element'] = input("Input the beast ELement> ").strip().title()
          if characteristics['Element'].strip().lower() not in elements:
            continue
          else: 
            break
    elif count == 4:
      while True:
        try:
          int(characteristics['MP'])
          break
        except:
          print()
          print(f"{colors('red')}Error, Can't recognize this number! Please try again{colors('reset')}")
          print(f"{colors('magenta')}")
          characteristics['MP'] = input("Input the beast MP: ")
          continue
          
        
      if int(characteristics['MP']) < 0 or int(characteristics['MP']) > 100:
        while True:
          print()
          print(f"{colors('red')}Error, Please make sure it's a number between 0 and 100!{colors('reset')}")
          print(f"{colors('magenta')}")
          characteristics['MP'] = input("Input the beast MP: ")
          if int(characteristics['MP']) < 0 or int(characteristics['MP']) > 100:
            continue
          else:
            break
    elif count == 3:
      while True:
        try:
          int(characteristics['HP'])
          break
        except:
          print()
          print(f"{colors('red')}Error, Can't recognize this number! Please try again{colors('reset')}")
          print(f"{colors('green')}")
          characteristics['HP'] = input("Input the beast HP: ")
          continue
      if int(characteristics['HP']) < 0 or int(characteristics['HP']) > 100:
        while True:
          print()
          print(f"{colors('red')}Error, Please make sure it's a number between 0 and 100!{colors('reset')}")
          print(f"{colors('green')}")
          characteristics['HP'] = input("Input the beast HP: ")
          if int(characteristics['HP']) < 0 or int(characteristics['HP']) > 100:
            continue
          else:
            break  
  beasts[beast_name] = characteristics
  print()
  print()
  prettyprint()
  
  while True:
    print(f"{colors('yellow')}")
    print("\033[?25h",end="")
    again = input("Add another (y/n)? > ")
    if again.lower().strip() == 'n':
      print("\033[?25l")
      spaces('>15')
      print(f"{colors('cyan')}Thanks for playing!")
      print()
      print()
      time.sleep(1)
      exit()
    elif again.lower().strip() == 'y':
      os.system('clear')
      home()
    else:
      print()
      print(f"{colors('red')}Error! Please try again")
      continue
      
  

  
      
        
      
  

home()
