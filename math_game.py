print("\033[36m""Math Game!""\033[0m")
print()
while True:
  try:
    number = int(input("Input your multiples: "))
    break
  except ValueError:
    print("\033[31m""Please try again with a valid input!""\033[0m")
    continue
print()

for i in range(1,11):
  ans = i * number
  while True:
    try:
      ask = int(input(f"{i} X {number} = "))
      break
    except ValueError:
      print("\033[31m""Please try again with a valid input!""\033[0m")
      continue
  if ask != ans:
    print()
    print("\033[31m"f"Nope! that was {ans}""\033[0m")
    break
  else: 
    print("\033[32m""Great work!""\033[0m")
    print()

if i == 10:
  print()
  print()
  print("---")
  print("\033[36m""WOW YOU SCORED A WHOPPING 10 OUT OF 10!!! 💯😲""\033[0m")
else:
  print()
  print()
  print("---")
  print("\033[33m"f"You scored {i} out of 10""\033[0m")
  