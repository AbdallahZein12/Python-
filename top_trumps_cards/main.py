import time, sys, os, random, threading

from PIL import Image


player1_counter = 0
player2_counter = 0
cards__ = {}

def colors(col):
  if col == 'red':
    return '\033[31m'
  elif col == 'blue':
    return '\033[34m'
  elif col == 'green':
    return '\033[32m'
  elif col == 'yellow':
    return '\033[33m'
  elif col == 'black':
    return '\033[30m'
  elif col == 'magenta':
    return '\033[35m'
  elif col == 'cyan':
    return '\033[36m'
  else:
    return '\033[0m'


def space(pos):
  space_ = ''
  print(f"{space_:{pos}}", end='')


def roller(min, max):
  num = random.randint(min, max)
  return num


def random_col():
  colors_list = ['red', 'blue', 'green', 'yellow', 'black', 'magenta', 'cyan']
  return random.choice(colors_list)


def char_printer(string):
  for i in string:
    print(f"{colors(random_col())}{i}", end='', sep='')
    time.sleep(0.1)
    sys.stdout.flush()

def billboard(string,timer):
    counter_ = 0
    while counter_ != timer:
      for i in string:
        print(colors(random_col()), i, end='')
      print()
      sys.stdout.write("\033[F")
      counter_ += 1


def option_2():
  global player1_counter
  global player2_counter
  
  print("\033[?25l")
  count = 1
  os.system('cls')
  cards = {
    'Neymar': {
      'Goals': 52,
      'Caps': 81,
      'Trophies': 15,
      'Stars': '4.5/5'
    },
    'Ronaldo': {
      'Goals': 79,
      'Caps': 147,
      'Trophies': 24,
      'Stars': '5/5'
    },
    'Messi': {
      'Goals': 61,
      'Caps': 122,
      'Trophies': 29,
      'Stars': '5/5'
    },
    'Luis Suarez': {
      'Goals': 49,
      'Caps': 95,
      'Trophies': 14,
      'Stars': '4.5/5'
    },
    'Paulo Dybala': {
      'Goals': 0,
      'Caps': 10,
      'Trophies': 6,
      'Stars': '3.5/5'
    },
    'Lewendowlski': {
      'Goals': 51,
      'Caps': 89,
      'Trophies': 13,
      'Stars': '5/5'
    },
    'Harry Kane': {
      'Goals': 12,
      'Caps': 23,
      'Trophies': 0,
      'Stars': '3.5/5'
    },
    'Eden Hazard': {
      'Goals': 20,
      'Caps': 80,
      'Trophies': 6,
      'Stars': '4/5'
    },
    'Dele Alli': {
      'Goals': 2,
      'Caps': 22,
      'Trophies': 0,
      'Stars': '3/5'
    },
    'Paul Pogba': {
      'Goals': 8,
      'Caps': 49,
      'Trophies': 8,
      'Stars': '4/5'
    },
    'Manuel Neuer': {
      'Goals': 0,
      'Caps': 74,
      'Trophies': 16,
      'Stars': '4.5/5'
    }
  }

  for name, items in cards.items():
    if count % 2 == 0:
      time.sleep(0.2)
      print("{:>25}".format(name))
      count += 1
    else:
      print()
      time.sleep(0.2)
      print("{:>15}".format(name), end='')
      sys.stdout.flush()
      count += 1

  print()
  print()
  print()
  print()
  space('>17')
  char_printer('PLAYER 1')
  print()
  print()

  

  billboard('  PRESS ENTER TO ROLL',1000)
  print()
  print()
  
  user_input1 = input("")

  number = roller(0, len(cards)-1)

  if number == 1:
    print(f"{colors('blue')}")
    with Image.open('Ronaldo.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()

    print()
    print()
    space('>15')
    print('RONALDO')
    print()
    print()
    print()

  elif number == 0:
    print(f"{colors('blue')}")
    with Image.open('Neymar.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('NEYMAR')
    print()
    print()
    print()
  elif number == 2:
    print(f"{colors('blue')}")
    with Image.open('Messi.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('MESSI')
    print()
    print()
    print()
  elif number == 3:
    print(f"{colors('blue')}")
    with Image.open('Suarez.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('LUIS SUAREZ')
    print()
    print()
    print()
  elif number == 4:
    print(f"{colors('blue')}")
    with Image.open('Paulo.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('PAULO DYBALA')
    print()
    print()
    print()
  elif number == 5:
    print(f"{colors('blue')}")
    with Image.open('Lewendowlski.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('lEWENDOWLSKI')
    print()
    print()
    print()
  elif number == 6:
    print(f"{colors('blue')}")
    with Image.open('Kane.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('KANE')
    print()
    print()
    print()
  elif number == 7:
    print(f"{colors('blue')}")
    with Image.open('Hazard.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print("HAZARD")
    print()
    print()
    print()
  elif number == 8:
    print(f"{colors('blue')}")
    with Image.open('dele-alli.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('DELLE ALLI')
    print()
    print()
    print()
  elif number == 9:
    print(f"{colors('blue')}")
    with Image.open('Pogba.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('PAUL POGBA')
    print()
    print()
    print()
  elif number == 10:
    print(f"{colors('blue')}")
    with Image.open('Neuer.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('NEUER')
    print()
    print()
    print()


  space('>17')
  char_printer('PLAYER 2')
  print()
  print()
  billboard('  PRESS ENTER TO ROLL',1000)
  print()
  print()
    
  user_input2 = input("")
  while True:
    number2 = roller(0, len(cards)-1)
    if number2 == number:
      continue
    else:
      break
    
  if number2 == 1:
    print(f"{colors('red')}")
    with Image.open('Ronaldo.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('RONALDO')
    print()
    print()
    print()

  elif number2 == 0:
    print(f"{colors('red')}")
    with Image.open('Neymar.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('NEYMAR')
    print()
    print()
    print()
  elif number2 == 2:
    print(f"{colors('red')}")
    with Image.open('Messi.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('MESSI')
    print()
    print()
    print()
  elif number2 == 3:
    print(f"{colors('red')}")
    with Image.open('Suarez.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('LUIS SUAREZ')
    print()
    print()
    print()
  elif number2 == 4:
    print(f"{colors('red')}")
    with Image.open('Paulo.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('PAULO DYBALA')
    print()
    print()
    print()
  elif number2 == 5:
    print(f"{colors('red')}")
    with Image.open('Lewendowlski.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('lEWENDOWLSKI')
    print()
    print()
    print()
  elif number2 == 6:
    print(f"{colors('red')}")
    with Image.open('Kane.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('KANE')
    print()
    print()
    print()
  elif number2 == 7:
    print(f"{colors('red')}")
    with Image.open('Hazard.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print("HAZARD")
    print()
    print()
    print()
  elif number2 == 8:
    print(f"{colors('red')}")
    with Image.open('dele-alli.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('DELLE ALLI')
    print()
    print()
    print()
  elif number2 == 9:
    print(f"{colors('red')}")
    with Image.open('Pogba.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('PAUL POGBA')
    print()
    print()
    print()
  elif number2 == 10:
    print(f"{colors('red')}")
    with Image.open('Neuer.jpg') as im:
      im = im.convert('L')
      im = im.resize((80,60))
      chars = '.:-=+*#%@'
      for y in range(im.size[1]):
        time.sleep(0.05)
        for x in range(im.size[0]):
          gray = im.getpixel((x,y))
          char = chars[gray * len(chars) // 355]

          print(char,end='')
        print()
    print()
    print()
    space('>15')
    print('NEUER')
    print()
    print()
    print()
    
  print(colors('yellow'))
  count_ = 1
  for i in cards['Dele Alli']:
    if count_ % 2 == 0:
      time.sleep(0.7)
      print("{:>25}".format(i))
      count_ += 1
    else:
      time.sleep(0.7)
      print()
      print("{:>15}".format(i), end='')
      sys.stdout.flush()
      count_ += 1

  print()
  print()
  print()
  time.sleep(0.7)
  billboard('               PICKING CATEGORY',100000)

  os.system('cls')
  
  space('>30')
  cat = roller(0,len(cards['Dele Alli'])-1)
  keys = list(cards['Dele Alli'].keys())
  time.sleep(0.5)
  print('Your Category is')
  print()
  print()
  billboard('               loading',10000)
  print()
  print()
  print()
  space('>30')
  print('     ',end='')
  char_printer(keys[cat])
  category = keys[cat]
  players = list(cards.keys())

  print()
  print()
  print(colors('blue'),players[number],'       ',end='')
  sys.stdout.flush()
  time.sleep(1)
  print(colors('red'),players[number2])
  print()
  print()
  time.sleep(1)
  print(colors('blue'))
  print(keys[cat],'              ',end='')
  sys.stdout.flush()
  time.sleep(1)
  print(colors('red'),keys[cat])
  print()
  print()
  
  player1_player = players[number]
  player2_player = players[number2]
  if keys[cat] == 'Stars':
    slash_index1 = cards[player1_player][category].index('/')
    slash_index2 = cards[player2_player][category].index('/')
    player1_stars = cards[player1_player][category][:slash_index1]
    player2_stars = cards[player2_player][category][:slash_index2]
    if player1_stars > player2_stars:
      time.sleep(1)
      print(colors('green'),cards[player1_player][category],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('yellow'),'                 ',cards[player2_player][category])
      print()
      print()
      print()
      space('>10')
      print(colors('blue'),'Player1 Wins!')
      player1_counter += 1
      print()
      print()
      print()
 
    elif player1_stars < player2_stars:
      time.sleep(1)
      print(colors('yellow'),cards[player1_player][category],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('green'),'                 ',cards[player2_player][category])
      print()
      print()
      print()
      space('>10')
      print(colors('red'),'Player2 Wins!')
      player2_counter += 1
      print()
      print()
      print()
   
    else:
      time.sleep(1)
      print(colors('yellow'),cards[player1_player][category],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('yellow'),'                 ',cards[player2_player][category])
      print()
      print()
      print()
      space('>10')
      print(colors('yellow'),'DRAW!')
      print()
      print()
      print()
     
  else:
    if cards[player1_player][category] > cards[player2_player][category]:
      time.sleep(1)
      print(colors('green'),cards[player1_player][category],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('yellow'),'                 ',cards[player2_player][category])
      print()
      print()
      print()
      space('>10')
      print(colors('blue'),'Player1 Wins!')
      player1_counter += 1
      print()
      print()
      print()
    

    elif cards[player1_player][category] < cards[player2_player][category]:
      time.sleep(1)
      print(colors('yellow'),cards[player1_player][category],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('green'),'                 ',cards[player2_player][category])
      print()
      print()
      print()
      space('>10')
      print(colors('red'),'Player2 Wins!')
      player2_counter += 1
      print()
      print()
      print()
      

    else:
      time.sleep(1)
      print(colors('yellow'),cards[player1_player][category],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('yellow'),'                 ',cards[player2_player][category])
      print()
      print()
      print()
      space('>10')
      print(colors('yellow'),'DRAW!')
      print()
      print()
      print()
  print(colors('blue'),'Player 1: ',player1_counter,end='')
  sys.stdout.flush()
  print('                 ',colors('red'),'Player 2: ',player2_counter)
  print()
  print()
  print(colors('yellow'))
  print('\033[?25h')
  reset = input('Play again?(y/n)> ')
  if reset.lower().strip() == 'y':
    os.system('cls')
    option_2()
  elif reset.lower().strip() == 'n':
    player1_counter = 0
    player2_counter = 0
    os.system('cls')
    home()

  
def random_battle():
  print('\033[?25l')
  global player1_counter
  global player2_counter
  os.system('cls')
  players_custom = list(cards__.keys())
  choice = roller(0,len(cards__)-1)

  count__ = 1
  for name, items in cards__.items():
    if count__ % 2 == 0:
      time.sleep(0.2)
      print("{:>25}".format(name))
      count__ += 1
    else:
      print()
      time.sleep(0.2)
      print("{:>15}".format(name), end='')
      sys.stdout.flush()
      count__ += 1
  print()
  print()
  print()
  print()
  space('>17')
  char_printer('PLAYER 1')
  print()
  print()
  billboard('  PRESS ENTER TO ROLL',1000)
  print()
  print()
  user_input_1 = input("")
  print(colors('blue'))
  print()
  space('>15')
  print(players_custom[choice])
  print()
  print()
  print()
  space('>17')
  char_printer('PLAYER 2')
  print()
  print()
  billboard('  PRESS ENTER TO ROLL',1000)
  print()
  print()
  while True:
    choice2 = roller(0,len(cards__)-1)
    if choice2 == choice:
      continue
    else:
      break
  user_input_2 = input('')
  print(colors('red'))
  print()
  space('>15')
  print(players_custom[choice2])
  print()
  print()
  print()
  print(colors('yellow'))
  count_____ = 1
  for i in cards__[players_custom[0]]:
    if count_____ % 2 == 0:
      time.sleep(0.7)
      print("{:>25}".format(i))
      count_____ += 1
    else:
      time.sleep(0.7)
      print()
      print("{:>15}".format(i), end='')
      sys.stdout.flush()
      count_____ += 1

  print()
  print()
  print()
  time.sleep(0.7)
  billboard('               PICKING CATEGORY',100000)
  os.system('cls')
  space('>30')
  cat_ = roller(0,len(cards__[players_custom[0]])-1)
  categories = list(cards__[players_custom[0]])
  time.sleep(0.5)
  print('Your Category is')
  print()
  print()
  billboard('               loading',10000)
  print()
  print()
  print()
  space('>30')
  print('     ',end='')
  char_printer(categories[cat_])
  category_ = categories[cat_]
  print()
  print()
  print(colors('blue'),players_custom[choice],'       ',end='')
  sys.stdout.flush()
  time.sleep(1)
  print(colors('red'),players_custom[choice2])
  print()
  print()
  time.sleep(1)
  print(colors('blue'))
  print(categories[cat_],'              ',end='')
  sys.stdout.flush()
  time.sleep(1)
  print(colors('red'),categories[cat_])
  print()
  print()
  player1_player_ = players_custom[choice]
  player2_player_ = players_custom[choice2]
  if categories[cat_] == 'Stars':
    slash_index1_ = cards__[player1_player_][category_].index('/')
    slash_index2_ = cards__[player2_player_][category_].index('/')
    player1_stars_ = cards__[player1_player_][category_][:slash_index1_]
    player2_stars_ = cards__[player2_player_][category_][:slash_index2_]
    if player1_stars_ > player2_stars_:
      time.sleep(1)
      print(colors('green'),cards__[player1_player_][category_],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('yellow'),'                 ',cards__[player2_player_][category_])
      print()
      print()
      print()
      space('>10')
      print(colors('blue'),'Player1 Wins!')
      player1_counter += 1
      print()
      print()
      print()
 
    elif player1_stars_ < player2_stars_:
      time.sleep(1)
      print(colors('yellow'),cards__[player1_player_][category_],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('green'),'                 ',cards__[player2_player_][category_])
      print()
      print()
      print()
      space('>10')
      print(colors('red'),'Player2 Wins!')
      player2_counter += 1
      print()
      print()
      print()
   
    else:
      time.sleep(1)
      print(colors('yellow'),cards__[player1_player_][category_],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('yellow'),'                 ',cards__[player2_player_][category_])
      print()
      print()
      print()
      space('>10')
      print(colors('yellow'),'DRAW!')
      print()
      print()
      print()
  else:
    if cards__[player1_player_][category_] > cards__[player2_player_][category_]:
      time.sleep(1)
      print(colors('green'),cards__[player1_player_][category_],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('yellow'),'                 ',cards__[player2_player_][category_])
      print()
      print()
      print()
      space('>10')
      print(colors('blue'),'Player1 Wins!')
      player1_counter += 1
      print()
      print()
      print()
    

    elif cards__[player1_player_][category_] < cards__[player2_player_][category_]:
      time.sleep(1)
      print(colors('yellow'),cards__[player1_player_][category_],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('green'),'                 ',cards__[player2_player_][category_])
      print()
      print()
      print()
      space('>10')
      print(colors('red'),'Player2 Wins!')
      player2_counter += 1
      print()
      print()
      print()
      

    else:
      time.sleep(1)
      print(colors('yellow'),cards__[player1_player_][category_],end='')
      sys.stdout.flush()
      time.sleep(1)
      print(colors('yellow'),'                 ',cards__[player2_player_][category_])
      print()
      print()
      print()
      space('>10')
      print(colors('yellow'),'DRAW!')
      print()
      print()
      print()
  print(colors('blue'),'Player 1: ',player1_counter,end='')
  sys.stdout.flush()
  print('                 ',colors('red'),'Player 2: ',player2_counter)
  print()
  print()
  print(colors('yellow'))
  reset = input('Play again?(y/n)> ')
  if reset.lower().strip() == 'y':
    os.system('cls')
    random_battle()
  elif reset.lower().strip() == 'n':
    player1_counter = 0
    player2_counter = 0
    os.system('cls')
    home()




  

  
  

def option_1():
  
  add_more = 'y'
  while add_more.lower().strip() == 'y':
    print(colors('yellow'))
    player = input('Input your player> ')
    player_ = player.title().strip()
    print('\033[?25l')
    os.system('cls')
    time.sleep(0.5)
    print(player_)
    print()
    print()
    print('\033[?25h')
    while True:
      try:
        goals = input(f"Input goals for {player_}> ")
        int(goals)
        break
      except:
        print()
        print(colors('red'),'Error! Please try again',colors('yellow'))
        print()
        continue
    print('\033[?25l')
    os.system('cls')
    time.sleep(0.5)
    print(player_)
    print()
    time.sleep(0.5)
    print('Goals: ',goals)
    print()
    print()
    print('\033[?25h')
    while True:
      try:
        caps = input(f'Input caps for {player_}> ')
        int(caps)
        break
      except:
        print()
        print(colors('red'),'Error! Please try again',colors('yellow'))
        print()
        continue
    print('\033[?25l')
    os.system('cls')
    time.sleep(0.5)
    print(player_)
    print()
    time.sleep(0.5)
    print('Goals:', goals)
    print()
    time.sleep(0.5)
    print('Caps: ',caps)
    print()
    print()
    print('\033[?25h')
    while True:
      try:
        trophies = input(f'Input trophies for {player_}> ')
        int(trophies)
        break
      except:
        print()
        print(colors('red'),'Error! Please try again',colors('yellow'))
        print()
        continue
    print('\033[?25l')
    os.system('cls')
    time.sleep(0.5)
    print(player_)
    print()
    time.sleep(0.5)
    print('Goals: ',goals)
    print()
    time.sleep(0.5)
    print('Caps: ', caps)
    print()
    time.sleep(0.5)
    print('Trophies: ',trophies)
    print()
    print()
    print('\033[?25h')
    while True:
      stars_ = input(f'Input stars of out 5 for {player_}> ')
      try:
        new_stars = int(stars_)
      except:
        try:
          new_stars = float(stars_)
        except:
          print()
          print(colors('red'),'Error! Please try again!',colors('yellow'))
          print()
          continue
      if type(new_stars) == int:
        if int(new_stars) > 5:
          print()
          print(colors('red'),'Error! Please try again!',colors('yellow'))
          print()
          continue
        else:
          break
      elif type(new_stars) == float:
        if float(new_stars) > 5.0:
          print()
          print(colors('red'),'Error! Please try again!',colors('yellow'))
          print()
          continue
        else:
          break
      else:
        print()
        print(colors('red'),'Error! Please try again!',colors('yellow'))
        print()
        continue
    print('\033[?25l')
      
    os.system('cls')
    time.sleep(0.5)
    print(player_)
    print()
    time.sleep(0.5)
    print('Goals: ',goals)
    print()
    time.sleep(0.5)
    print('Caps: ',caps)
    print()
    time.sleep(0.5)
    print('Trophies: ',trophies)
    print()
    time.sleep(0.5)
    print(f'Stars: {stars_}/5')
    print()
    print()
    cards__[player_] = {
      'Goals':goals,
      'Caps':caps,
      'Trophies':trophies,
      'Stars':f'{new_stars}/5'
    }
    if len(cards__) < 2:
      print(colors('blue'),'Warning! you must have more than one player to battle with custom cards',(colors('yellow')))
      print('\033[?25h')
      option_1()
    else:
      print('\033[?25l')
      print()
      print() 
      time.sleep(0.5)
      print('1-Add More          ',end='')
      sys.stdout.flush()
      time.sleep(0.5)
      print(colors('red'),'2-Battle With Custom Cards ⚔️          ',end='')
      sys.stdout.flush()
      time.sleep(0.5)
      print(colors('green'),'3-Go Home🏠          ',end='')
      sys.stdout.flush()
      time.sleep(0.5)
      print(colors('magenta'),'4-Clear List 💣')
      print()
      print()
      print('\033[?25h')
      print(colors('yellow'))
      while True:
        user__ = input('> ')
        try: 
          new_user__ = int(user__)
        except:
          print()
          print(colors('red'),'Error! Please try again!',colors('yellow'))
          print()
          continue
        if new_user__ == 3:
          os.system('cls')
          home()
        elif new_user__ == 1:
          os.system('cls')
          print('\033[?25h')
          option_1()
        elif new_user__ == 2:
          print('\033[?25l')
          random_battle()
        elif new_user__ == 4:
          os.system('cls')
          cards__.clear()
          print('\033[?25l')
          print(colors('green'),'List Cleared!',colors('yellow'))
          print()
          print() 
          time.sleep(0.5)
          print('1-Add More          ',end='')
          sys.stdout.flush()
          time.sleep(0.5)
          print(colors('red'),'2-Battle With Custom Cards ⚔️          ',end='')
          sys.stdout.flush()
          time.sleep(0.5)
          print(colors('green'),'3-Go Home🏠          ')
          print()
          print()
          print('\033[?25h')
          print(colors('yellow'))
          while True:
            user__ = input('> ')
            try: 
              new_user__ = int(user__)
            except:
              print()
              print(colors('red'),'Error! Please try again!',colors('yellow'))
              print()
              continue
            if new_user__ == 3:
              os.system('cls')
              home()
            elif new_user__ == 1:
              os.system('cls')
              print('\033[?25h')
              option_1()
            elif new_user__ == 2:
              print('\033[?25l')
              random_battle()
            else:
              print()
              print(colors('red'),'Error! Please try again!',colors('yellow'))
              print()
              continue 
        else:
          print()
          print(colors('red'),'Error! Please try again!',colors('yellow'))
          print()
          continue 


          
      

      

    


    
        
    
    

    


    
  
  


  
    


    

def home():
  print('\033[?25l', end='')
  space('>20')
  char_printer('FIFA TRUMPS CARDS')
  create = '1- Create Trump Cards!'
  random_ = '2- Battle With Random Cards'
  print()
  print()
  print()
  print()
  space('>0')
  print(f"{colors(random_col())}{create}", end='')
  space('>13')
  print(f"{colors(random_col())}{random_}")
  print(f"{colors('yellow')}")
  print('\033[?25h')
  user = input("Pick A Number> ")

  if int(user) == 2:
    option_2()
  elif int(user) == 1:
    os.system('cls')
    option_1()



home()

