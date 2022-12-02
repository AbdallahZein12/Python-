import random, os, time 

def roller(sides):
  roll = random.randint(1,sides)
  return roll 


def health():
  six_roll = roller(6)
  twelve_roll = roller(12)

  hea = ((six_roll * twelve_roll) / 2) + 10

  return hea

def strength():
  six_roll = roller(6)
  twelve_roll = roller(8)

  stre = ((six_roll * twelve_roll) / 2) + 12

  return stre 


ans = "yes"
while ans == "yes":
  print("Character Builder ⚔️")
  print()
  time.sleep(1)
  charname1 = input("\033[36m""Name your legend: ""\033[0m")
  print()
  while True:
    chartype1 = input("\033[37m""Character type (Human, Elf, Wizard, Orc): ""\033[0m")
    if chartype1 != "Human" and chartype1 and "Elf" and chartype1 != "Wizard" and chartype1 != "Orc" and chartype1 != "human" and chartype1 != "elf" and chartype1 != "wizard" and chartype1 != "orc":
      print("\033[31m""Please try again""\033[0m")
      continue
    else:
      os.system("clear")
      print(f"{charname1}, the {chartype1}")
      break
  
  print()
  time.sleep(1)
  print("Who are they batteling? ⚔️")
  print()
  time.sleep(1)
  charname2 = input("\033[37m""Name your legend: ""\033[0m")
  print()
  while True:
    chartype2 = input("\033[37m""Character type (Human, Elf, Wizard, Orc): ""\033[0m")
    if chartype2 != "Human" and chartype2 and "Elf" and chartype2 != "Wizard" and chartype2 != "Orc" and chartype2 != "human" and chartype2 != "elf" and chartype2 != "wizard" and chartype2 != "orc":
      print("\033[31m""Please try again""\033[0m")
      continue
    else:
      os.system("clear")
      time.sleep(1)
      break
      
  print(f"           {charname1}, the {chartype1}")
  health1 = health()
  strength1 = strength()
  print("            HEALTH: ", health1)
  strength5 = print("           STRENGTH: ", strength1)
  print()
  time.sleep(1)
  print("                VS")
  print()
  time.sleep(1)
  print(f"           {charname2}, the {chartype2}")
  health2 = health()
  strength2 = strength()
  time.sleep(1)
  health3 = print("            HEALTH: ", health2)
  strength3 = print("          STRENGTH: ", strength2)
      

  counter = 1
  winner = None

  while True:
    time.sleep(1)
    os.system("clear")
    print("TIME TO FIGHT 🤺")

    c1roll = roller(6)
    c2roll = roller(6)

    difference = abs(strength1 - strength2) + 1 

    if c1roll > c2roll:
      health2 -= difference
      if round == 1 :
        print(charname1, "wins the first blow!")
      else:
        print(charname1, "wins round", counter)
    elif c2roll > c1roll:
      health1 -= difference 
      if round ==1:
        print(charname2, "wins the first blow")
      else:
        print(charname2, "wins round", counter)
    else:
      print("They both clash and draw round, ", counter)

    print()
    print(charname1)
    print("HEALTH: ", health1)
    print()
    print(charname2)
    print("HEALTH: ", health2)
    print()

    if health1 <= 0 :
      print(charname1, "has died!")
      winner = charname2
      break
    elif health2 <=0:
      print(charname2, "has died!")
      winner = charname1
      ans = input("Would you like to play again? ")
    else:
      print("They are both standing!")
      counter += 1 

    time.sleep(1)
    os.system("clear")
    print("BATTLE TIME 🤺")
    print()
    print(winner, 'has won in', counter, "rounds")
    
  
      #elif health <= 0:
     # os.system("clear")
      #print(f"{charname} has been destroyed!")
      #time.sleep(1)
      #print(f"{charname1} the {chartype1} has won in {counter} rounds")
      #repeat()
    #else: 
      #print("They are both standing!")
      #print()
      #continue
  
  
          
      
          

     
    ##elif health2() >= 0:
     # os.system("clear")
    #  print(f"{charname1} has been destroyed!")
      #time.sleep(1)
     # print(f"{charname} the {chartype} has won in {counter} rounds")
     # repeat()
   # elif health2 > 0: 
      #print("They are both standing!")
      #continue