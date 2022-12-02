import random 
def dice(sides):
  while True:
    randoms = random.randint(1,sides)
    print("\033[32m"f"You rolled a {randoms}""\033[0m")
    ask = input("Roll again? ")
    if ask == "Y" or ask == "y":
      continue
    else:
      ask1 = input("Roll again with different sides? ")
      if ask1 == "Y" or ask1 == "y":
        break
      else:
        print("Thank you for playing!")
        exit()


while True:
      try:
        sides = int(input("How many sides? "))
        dice(sides)
      except ValueError:
        print("\033[31m""Please Try Again With A Whole Number!""\033[0m")
        continue


print("\033[37m""Thank you for playing!""\033[0m")
    
  
  
  
