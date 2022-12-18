import os, time
list=[]

def col(color):
  if color == "red":
    return "\033[31m"
  elif color == "blue":
    return "\033[34m"
  elif color == "yellow":
    return "\033[33m"
  elif color == "green":
    return "\033[32m"
  elif color == "magenta":
    return "\033[35m"
  else:
    return "\033[0m"



def home():
  os.system('clear')
  print("\033[?25l", end='')
  title = f"{col('red')}={col('blue')}={col('reset')}= TODO List! {col('reset')}={col('blue')}={col('red')}="
  print(f"{title: >70}")
  print()
  print()
  
  time.sleep(0.3)
  view = f"{col('blue')} View"
  print(f"{view: >10}", end='')
  
  
  add = f"{col('green')} Add"
  print(f"{add: >15}", end='')
  
  
  remove = f"{col('red')} Remove"
  print(f"{remove: >20}", end='')

  clear = f"{col('magenta')} Clear"
  print(f"{clear: >18}", end='')
  
  edit = f"{col('yellow')} Edit"
  print(f"{edit: >19}", end='')

  print()
  while True:
    print("\033[?25h")
    user = input(f"{col('reset')}>")
  
    if user == 'view' or user == "View":
      os.system('clear')
      print("\033[?25l", end='')
      col('blue')
      
      for index in range (len(list)):
        print(f"{index}: {list[index]}")
        time.sleep(0.3)
  
      user1 = input("Press any key to go back to home!")
      
      home()
  
    
    elif user == 'add' or user == 'Add':
      def addi():
        os.system('clear')
        print("\033[?25l", end='')
      
        for index in range (len(list)):
          print(f"{col('reset')}{index}: {list[index]}")
          time.sleep(0.3)
        print()
        print()
        
        print("\033[?25h")
  
        while True:
          adder = input(f"{col('reset')}What would you like to add: ")
          if adder in list:
            print()
            print(f"{col('red')}Opps! Looks like this is already in the list")
            print("")
            continue 
          else: 
            list.append(adder)
            print()
            print(f"{col('green')}Successfully added [{adder}] to the list!")
            print()
  
            while True:
              again = input(f"{col('yellow')}Would you like to add some more: (y/n) ")
              if again == 'y' or again == 'Y':
                addi()
              elif again == 'n' or again == 'N':
                home()
              else:
                print()
                print(f"{col('red')}Opps! I didn't get that, try again!")
                print()
                continue
      addi()
  
    elif user == 'remove' or user == 'Remove':
      def remover():
        os.system('clear')
        print("\033[?25l", end='')
      
        for index in range (len(list)):
          print(f"{col('reset')}{index}: {list[index]}")
          time.sleep(0.3)
        print()
        print()
        print('\033[?25h')
        print()
        print()
        
        print("\033[?25h")
        while True:
          remove1 = input(f"{col('reset')}What item number would you like to remove: ")
          try:
            remove1 = int(remove1)
            break

          except ValueError:
            print()
            print(f"{col('red')}Opps! I didn't get that, try again!")
            print()
            continue
        
      
         
        while True:
          print()
          ask1 = input(f"{col('yellow')}Are you sure you want to delete item # {remove1}: (y/n) ")
          
          if ask1 == 'y' or ask1 == 'Y':
            try:
              del list[remove1]
            
            except IndexError:
              print()
              print(f"{col('red')}Oops, looks like this item was not on the list")
              while True:
                print()
                homer = input(f"{col('yellow')}Would you like to return home: (y/n) ")
                if homer == 'y' or homer == 'Y':
                  home()
                elif homer == 'N' or homer == 'n':
                  remover()
                else:
                  print()
                  print(f"{col('red')}Opps! I didn't get that, try again!")
                  continue
                
              
            print()
            print(f"{col('green')}Successfully removed item # {remove1}")
            
            while True:
              print()
              homer = input(f"{col('yellow')}Would you like to return home: (y/n) ")
              if homer == 'y' or homer == 'Y':
                home()
              elif homer == 'N' or homer == 'n':
                remover()
              else:
                print()
                print(f"{col('red')}Opps! I didn't get that, try again!")
                continue
          elif ask1 == 'N' or ask1 == 'n':
            while True:
              print()
              homer = input(f"{col('yellow')}Would you like to return home: (y/n) ")
              if homer == 'y' or homer == 'Y':
                home()
              elif homer == 'N' or homer == 'n':
                remover()
              else:
                print()
                print(f"{col('red')}Opps! I didn't get that, try again!")
                continue
        
          
      remover()
    elif user == 'clear' or user == 'Clear' or user == 'CLEAR':
      def clearer():
        os.system('clear')
        sure = input(f"{col('yellow')}Are you sure you want to clear and reset your entire list: (y/n) ")
        if sure == 'y' or sure == 'Y':
          list.clear() 
          print()
          print(f"{col('green')}Successfully nuked the entire list 💣")
          while True:
            print()
            homer = input(f"{col('yellow')}Would you like to return home: (y/n) ")
            if homer == 'y' or homer == 'Y':
              home()
            elif homer == 'N' or homer == 'n':
              clearer()
            else:
                print()
                print(f"{col('red')}Opps! I didn't get that, try again!")
                continue
  
        elif sure == 'n' or sure == 'N':
          while True:
            print()
            homer = input(f"{col('yellow')}Would you like to return home: (y/n) ")
            if homer == 'y' or homer == 'Y':
              home()
            elif homer == 'N' or homer == 'n':
              clearer()
            else:
                print()
                print(f"{col('red')}Opps! I didn't get that, try again!")
                continue
        else:
          print(f"{col('red')}Sorry I didn't get that! Please try again")
          time.sleep(1.5)
          clearer()
      clearer()
  
    elif user == 'Edit' or user == 'edit':
      def editorr():
        os.system('clear')
        print("\033[?25l", end='')
      
        for index in range (len(list)):
          print(f"{col('reset')}{index}: {list[index]}")
          time.sleep(0.3)
        print()
        print()
        print('\033[?25h')
        while True:
          editor = input(f"{col('reset')}What item number would you like to edit: ")
          try:
            int(editor)
            break
          except ValueError:
            print()
            print(f"{col('red')}Opps! I didn't get that, try again!")
            print()
            continue
        
        os.system('clear')
        editor1 = input(f"{col('reset')}{editor}: ")
        while True:
          try:
            list[int(editor)] = editor1
            break
          except IndexError:
            print()
            print(f"{col('red')}Looks like this wasn't on the list!")
            while True:
              print()
              homer = input(f"{col('yellow')}Would you like to return home: (y/n) ")
              if homer == 'y' or homer == 'Y':
                home()
              elif homer == 'N' or homer == 'n':
                break
              else:
                print()
                print(f"{col('red')}Opps! I didn't get that, try again!")
                continue
            time.sleep(0.5)
            editorr()
  
        while True:
            print()
            homer = input(f"{col('yellow')}Would you like to return home: (y/n) ")
            if homer == 'y' or homer == 'Y':
              home()
            elif homer == 'N' or homer == 'n':
              editorr()
            else:
                print()
                print(f"{col('red')}Opps! I didn't get that, try again!")
                continue
      editorr()
    else:
      print()
      print(f"{col('red')}Opps! I didn't get that, try again!")
      print()
      continue
      

      
home()
  