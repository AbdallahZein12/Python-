from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stopplaying = int(input("Press 2 to pause at any time"))
    if stopplaying == 2:
      source.paused = True
      return 
    else: 
      continue
    # Start taking user input and doing something with it

while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("Awesome music player")
  time.sleep(1)
  print("Press 1 to start playing")
  time.sleep(1)
  print("Press 2 to exit")
  time.sleep(1)
  print("Press anyhting else to see the menu again")
  # take user's input
  user = int(input(""))
  if user == 1:
    os.system("clear")
    play()
  elif user == 2:
    exit()
  else:
    continue

  # check whether you should call the play() subroutine depending on user's input