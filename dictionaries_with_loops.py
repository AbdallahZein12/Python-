import time, os

def program():
  os.system('clear')
  printer = {"Name":"","URL":"","Description":"","Rating":""}
  
  time.sleep(0.5)
  print("\033[?25l",end="")
  print("\033[34m","Website Rating!! 🕸️","\033[0m",sep='')
  print("\033[?25h")
  print("\033[33m")
  time.sleep(0.5)
  website_name = input("Input the website name: ")
  printer["Name"] = website_name
  print()
  
  while True:
    URL = input("Input URL: ").strip().split()
    for elem in URL:
      if elem.isspace():
        URL.remove(elem)
    urljoined = ''.join(URL)
    break
  
  printer["URL"] = urljoined
  
    
  
  print()
  description = input("Input your description: ").strip()
  print()
  printer["Description"] = description
  
  while True:
    star_rating = input("Input the star rating out of 5: ")
    try:
      int(star_rating) 
    except:
      print()
      print("\033[31m","Please make sure your rating is a number anywhere from 1-5!","\033[0m")
      print("\033[33m")
      continue
    if int(star_rating) not in range(1,6):
      print()
      print("\033[31m","Please make sure your rating is a number anywhere from 1-5!","\033[0m")
      print("\033[33m")
      continue
    else:
      break
  
  
  printer["Rating"] = f"{star_rating}/5"
  os.system('clear')
  time.sleep(0.5)
  print("\033[34m",end="")
  for item, value in printer.items():
    print(f"{item}: {value}   ",end="",sep="")
  

  print()
  while True:
    print("\033[33m")
    ask1 = input("Would you like to try again? (y/n)> ")
    if ask1.lower().strip() == "y":
      program()
    elif ask1.lower().strip() == "n":
      print()
      print("\033[34m","Thank you for playing!","\033[0m",sep='')
      time.sleep(1)
      exit()
    else:
      print("\033[31m","Didn't catch that! Please try again.","\033[0m",end='')
      print()
      continue 

program()



      



