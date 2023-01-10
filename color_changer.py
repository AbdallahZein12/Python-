import os, time


def color_program():

  ans = "retry"
  while ans == "retry" or ans == "Retry":
    print("\033[?25h", end="")
    word = input("What is your word!: ")
    print("\033[?25l", end="")
    os.system("clear")
    time.sleep(0.5)
    print(word, "!")
    print()
    ans = input(
      "(If by any chance you want to change your word, just type Retry else press enter to continue!) ")
    print()
  print("\033[?25h", end="")
  color = input("What is your color> ")
  print("\033[?25l", end="")
  os.system("clear")

  if color == "red" or color == "Red":
    time.sleep(0.5)
    print("Super Subroutine!")
    print()
    time.sleep(0.5)
    print("With my""\033[31m"" new program ""\033[0m""I can just call red '", word, "' ", "and that word will appear in the color I set it to>>> " "\n" "\n" "\033[31m", word, "\033[0m" "\n""\n", "With no weird gaps!", "\n""\n", "Epic.", sep="", end="")
    print()
    print("\033[?25h", end="")

    while True:
      print()
      time.sleep(0.5)
      ans1 = input("Would you like to try again? ")
      if ans1 == "yes" or ans1 == "Yes":
        os.system("clear")
        color_program()
      else:
        os.system("clear")
        time.sleep(0.5)
        print("Thank you for playing!")
        exit()

  elif color == "green" or color == "Green":
    time.sleep(0.5)
    print("Super Subroutine!")
    print()
    time.sleep(0.5)
    print("With my""\033[0;32m"" new program ""\033[0m""I can just call green '", word, "' ", "and that word will appear in the color I set it to>>> " "\n" "\n" "\033[0;32m", word, "\033[0m" "\n""\n", "With no weird gaps!", "\n""\n", "Epic.", sep="", end="")
    print()
    print("\033[?25h", end="")
    
    while True:
      print()
      time.sleep(0.5)
      ans2 = input("Would you like to try again? ")
      if ans2 == "yes" or ans2 == "Yes":
        os.system("clear")
        color_program()
      else:
        os.system("clear")
        time.sleep(0.5)
        print("Thank you for playing!")
        exit()

  elif color == "blue" or color == "Blue":
    time.sleep(0.5)
    print("Super Subroutine!")
    print()
    time.sleep(0.5)
    print("With my""\033[0;34m"" new program ""\033[0m""I can just call blue '", word, "' ", "and that word will appear in the color I set it to>>> " "\n" "\n" "\033[0;34m", word, "\033[0m" "\n""\n", "With no weird gaps!", "\n""\n", "Epic.", sep="", end="")
    print()
    print("\033[?25h", end="")

    while True:
      
      print()
      time.sleep(0.5)
      ans3 = input("Would you like to try again? ")
      if ans3 == "yes" or ans3 == "Yes":
        os.system("clear")
        color_program()
      else:
        os.system("clear")
        time.sleep(0.5)
        print("Thank you for playing!")
        exit()

  else:
    print("\033[31m""Sorry! I don't recognize that color please try again""\033[0m")
    color_program()


    
color_program()
