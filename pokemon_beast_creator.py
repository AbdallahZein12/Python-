import time, os, random, sys


def colors(col):
  if col == "red":
    return "\033[31m"
  elif col == "green":
    return "\033[32m"
  elif col == "yellow":
    return "\033[33m"
  elif col == "blue":
    return "\033[34m"
  elif col == "magenta":
    return "\033[35m"
  else:
    return "\033[0m"


def program():
  dict = {"Name": "", "Type": "", "Move": "", "HP": "", "MP": ""}

  def seperator(x):
    colors1 = ["red", "green", "yellow", "blue", "magenta"]
    for char in x:
      y = random.choice(colors1)
      print(f"{colors(y)}{char}", end="")
      sys.stdout.flush()
      time.sleep(0.2)

  seperator("MokeBeast")
  list2 = ["earth", "fire", "air", "water", "spirit"]

  def inputer():
    print(f"{colors('yellow')}")
    print()
    input1 = input(
      "Input your beast's name, His type(earth,fire,air ,water, or spirit), his special move, starting HP and starting MP>  "
    )
    print(f"{colors('reset')}")
    if len(input1.split()) < 5 or len(input1.split()) > 5:
      print()
      print(
        f"{colors('red')} looks like your number of inputs is not matching! make sure you input all options and seperate them by a space!{colors('reset')}",
        end='')
      inputer()
    elif input1.split()[1] not in list2:
      print()
      print(
        f"{colors('red')}Oops! I can't seem to recognize your type, try again!{colors('reset')}"
      )
      inputer()
    try:
      int(input1.split()[3])
    except:
      print()
      print(
        f"{colors('red')}Oops! I can't seem to recognize any numbers for your HP, try again!{colors('reset')}"
      )
      inputer()
    try:
      int(input1.split()[4])
    except:
      print()
      print(
        f"{colors('red')}Oops! I can't seem to recognize any numbers for your MP, try again!{colors('reset')}"
      )
      inputer()
    else:
      lists = [word for word in input1.split()]
      dict["Name"] = lists[0]
      if lists[1].lower() == 'earth':
        dict["Type"] = f"{colors('green')}{lists[1].upper()}{colors('reset')}"
      elif lists[1].lower() == 'air':
        dict["Type"] = f"{colors('blue')}{lists[1].upper()}{colors('reset')}"
      elif lists[1].lower() == 'fire':
        dict["Type"] = f"{colors('red')}{lists[1].upper()}{colors('reset')}"
      elif lists[1].lower() == 'water':
        dict["Type"] = f"{colors('yellow')}{lists[1].upper()}{colors('reset')}"
      elif lists[1].lower() == 'spirit':
        dict[
          "Type"] = f"{colors('magenta')}{lists[1].upper()}{colors('reset')}"

      dict["Move"] = lists[2]

      dict["HP"] = lists[3]

      dict["MP"] = lists[4]

      for item, value in dict.items():
        print(item, " : ", value, end="\n\n")

    while True:
      print(f"{colors('yellow')}", end="")
      again = input("Try again? (y/n)> ")
      if again.lower().strip() == "y":
        os.system('clear')
        program()
      elif again.lower().strip() == "n":
        print()
        print()
        print(f"{colors('blue')}Thank you for playing!")
        time.sleep(1)
        exit()
      else:
        print()
        print(f"{colors('red')}Didn't catch that! Try again.")
        print()
        continue

  inputer()


program()
