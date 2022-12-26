import time, os

def add_dashes(string):
  result = list(string)
  i = 3
  counter = 0 
  while i < len(result):
    counter += 1 
    result.insert(i, '-')
    i += 4
    if counter == 2:
      break
  return "".join(result)

def add_slashes(string):
  result = list(string)
  i = 2
  counter = 0 
  while i < len(result):
    counter += 1 
    result.insert(i, '/')
    i += 3
    if counter == 2:
      break
  return "".join(result)

def program():
  contact_card = {"Name": "", "Date Of Birth": "" ,"TEL": "", "email": "", "address": ""}
  time.sleep(0.5)
  print("\033[25?",end='')
  print("\033[34m","Contact Card 📃","\033[0m", sep = "")
  time.sleep(0.5)
  print("\033[33m")
  contact_card["Name"] = input("Input your name> ").strip()
  time.sleep(0.5)
  print()
  contact_card["Date Of Birth"] = input("Input your date of birth> ").strip()
  if contact_card["Date Of Birth"][2] != '/' and contact_card["Date Of Birth"][5] != '/': 
    dob1 = add_slashes(contact_card["Date Of Birth"])
  else:
    dob1 = contact_card["Date Of Birth"]
  time.sleep(0.5)
  print()
  contact_card["TEL"] = input("Input your phone number> ").strip()
  if contact_card["TEL"][3] != "-" and contact_card["TEL"][7] != "-":
    telephone1 = add_dashes(contact_card["TEL"])
  else:
    telephone1 = contact_card["TEL"]
  
  time.sleep(0.5)
  print()
  contact_card["email"] = input("Input your email> ").strip()
  time.sleep(0.5)
  print()
  contact_card["address"] = input("Input your address> ")
  time.sleep(0.5)
  print()
  print("\033[0m",end='')
  time.sleep(0.7)
  os.system('clear')
  print(f"\033[34mHi {contact_card['Name']}. Our dictionary says that you were born on {dob1}, we can call you on {telephone1}, email {contact_card['email']}, or write to The Cupboard Under The Stairs, {contact_card['address']}\033[0m")
  

program()
