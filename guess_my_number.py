import random
print("Guess my number!!")
print()
counter = 0 

print("HINT--- It's between 1 and 100")
while True:
  myNumber = random.randint(1, 100)
  while True:
    try:
      print()
      guess = int(input("What do you think? "))
    except ValueError:
      print("\033[31m""Please try again with a whole number!""\033[0m")
      continue
    if guess > myNumber:
      print()
      print("\033[33m""Too high!""\033[0m")
      counter += 1 
      print(f"Number of attempts: {counter}")
      continue
      print()
    elif guess < myNumber:
      print()
      print("\033[33m""Too low!""\033[0m")
      counter += 1
      print(f"Number of attempts: {counter}")
      continue 
    else:
      print()
      print("\033[32m"f"Correct!!! My number was {myNumber}""\033[0m")
      print()
      print(f"Your number of attempts was: {counter}")
      counter = 0
      break
  print()
  cont = input("do you want to play again?(Y to confirm) ")
  if cont == "Y" or cont =="y":
    continue
  else:
    print()
    print("Thank you for playing!!")
    break

















#Totally Random One-Million-to-One

#What is your guess?: 500000
#Too low

#What is your guess?: 750000
#Too high

#What is your guess?: 600000
#Too low

#What is your guess?: 650000
#Correct!

#It took you 4 guesses to get the number correct.
#Click 'run' to try again with a different number.