import os,time
print('\033[33m',end='')
def check_list(lst):
  for char in lst:
    if char.isdigit():
      return True
f = open('high.score.txt', 'a+')
l = open('high.score.txt','r')
lin = l.readlines()
try:
  if lin[0] != 'Initials   :   Score\n':
    lin[0] = 'Initials   :   Score\n\n'
    l.close()
    l = open('high.score.txt','w')
    l.writelines(lin)
    l.close()
except:
  f.write('Initials   :   Score\n\n')

def main():
  os.system('cls')
  inputs = {
    'initials':None, 'score':None
  }
  for i,y in inputs.items():
    while True:
      print()
      inputs[i] = input(f"Input your {i}> ")
      if i == 'initials':
        if len(inputs[i]) > 3:
          print()
          print('\033[31m','Error, make sure initials are less than 3!','\033[33m')
          continue
        ans = check_list(inputs[i])
        if ans == True:
          print()
          print('\033[31m','Error, please try again!','\033[33m')
          continue
        else:
          break
               
        
        
            
        
          

    

      elif i == 'score':
        try:
          sc = int(inputs[i])
        except:
          print()
          print('\033[31m','Error, please try again!','\033[33m')
          print()
          continue
        if sc > 100000:
          print()
          print('\033[31m','Error, please try again!','\033[33m')
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
          print('\033[31m','Error, please try again!','\033[33m')
          print()
          continue
      

main()       
f.close()
        
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
    

  

