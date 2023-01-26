import os,time
f = open('high.score.txt', 'a+')
l = open('high.score.txt','r')
lin = l.readlines()
try:
  lin[0] == 'Initials   :   Score\n\n' 
except:
  lin[0] = "Initials   :   Score\n\n"
def main():
  inputs = {
    'initials':None, 'score':None
  }
  for i,y in inputs.items():
    while True:
      print()
      inputs[i] = input(f"Input your {i}> ")
      if i == 'initials':
        try: 
          initi = str(inputs[i])
          break
        except:
          continue
      elif i == 'score':
        try:
          sc = int(inputs[i])
        except:
          print()
          print('\033[31m','Error, please try again!','\033[0m')
          print()
          continue
        if sc > 100000:
          print()
          print('\033[31m','Error, please try again!','\033[0m')
          print()
          continue
        else:
          break
  c = 0
  for i,y in inputs.items():
    if c == 0:
      f.write(f"{y}    :    ")
      c+=1
    else: 
      f.write(f"{y}\n")
      print()
      again = input('Add more(y/n)?>  ')
      while True:
        if again.lower().strip() == 'n':
          print()
          print()
          print('Exiting...')
          time.sleep(2)
          exit()
        elif again.lower().strip() == 'y':
          os.system('cls')
          main()
        else:
          print()
          print('\033[31m','Error, please try again!','\033[0m')
          print()
          continue
      

main()       
        
        
  # if inputs[1] > 100000:
  #   print()
  #   print('\033[31m','Error, please try again!','\033[0m')
  #   print()
  #   while True:
  #     inputs[1] = input(f'Input your {inputs[1]}> ')
  #     if inputs[1] > 100000:
  #       print()
  #       print('\033[31m','Error, please try again!','\033[0m')
  #       print()
  #       continue
  #     else:
  #       break
    

  


