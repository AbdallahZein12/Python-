import time, os 
def colors(col):
  if col == 'red':
    return "\033[31m"
  elif col == 'blue':
    return "\033[34m"
  elif col == 'green':
    return "\033[32m"
  elif col == '':
    return "\033[0m"

def program():
  time.sleep(0.5)
  print(f"{colors('blue')}Star Wars Name Generator     ⚔️{colors('')}")
  time.sleep(1)
  print()
  user = input("Firstname, Lastname, Mother's Maiden Name, City You Were Born \n\n> ")

  list = user.split()

  list[0][0:3]
  SWFN = f"{list[0][0:3]}{list[1][0:3]} ".capitalize(),f"{list[2][0:2]}{list[3][:-4:-1]}".capitalize()
  print(f"{colors('green')}")
  time.sleep(0.5)
  print(''.join(SWFN))
  print(f"{colors('')}")
  print()
  while True:
    repeat = input("Go again (y/n)>  ").strip().lower()
    if repeat == "y":
      os.system('clear')
      program()
    elif repeat == "n":
      print()
      print(f"{colors('blue')}Thanks for playing!")
      time.sleep(1)
      exit()
    else:
      print()
      print(f"{colors('red')}Didn't get that. please try again!{colors('')}")
      print()
      continue 

program()