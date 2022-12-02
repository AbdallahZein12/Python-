print("\033[36m""Choose your increments!!""\033[0m")
print()
while True:
  while True:
    try:
      start = int(input("Start at: "))
      break
    except ValueError:
      print("\033[31m""Please Try Again!""\033[0m")
      continue
  print()
  
  while True:
    try:
      end = int(input("End before: "))
      break
    except ValueError:
      print("\033[31m""Please Try Again!""\033[0m")
  print()
  
  while True:
    try:
      increment = int(input("Increment between values: "))
      break
    except ValueError:
      print("\033[31m""Please Try Again!""\033[0m")
  print()
  
  for i in range(start, end, increment):
    print(i)
  
  print()
  cont = input("Would you like to continue?(Y to accept) ")
  if cont == "y" or cont == "Y":
    print()
    continue
  else:
    break
