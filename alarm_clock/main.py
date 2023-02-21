from playsound import playsound
import time
import sys
import os

colors_list_main = ['red','green','yellow']

class Color:

    @staticmethod
    def colorchng(string,col):
        colors_list_ = {
            "red":"\033[31m", "green":"\033[32m", "yellow":"\033[33m"
        }
        if col.strip().lower() in colors_list_:
            return f"{colors_list_[col]}{string}\033[0m"

def clock(seconds):
    count = 0
    print("\033[?25l",end='')
    os.system("cls")
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        count += 1
        odd_even = count % 2

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
    
        if time_left <= 5:
            if odd_even != 0:
                print(f"{minutes_left:02d}:{seconds_left:02d}")
                sys.stdout.write("\033[F")
            else:
                print("\033[31m",f"{minutes_left:02d}:{seconds_left:02d}","\033[0m",sep='')
                sys.stdout.write("\033[F")

        else:    
            print(f"{minutes_left:02d}:{seconds_left:02d}")
            sys.stdout.write("\033[F")
    
    playsound("alarm.mp3")

os.system('cls')

while True:
    try:
        print("\033[?25h",end='')
        print("\033[0m",end='')
        min_user = input("Input your minutes> ")
        min_user = int(min_user)
        break
    except ValueError:
        print()
        print(Color.colorchng("Error! Please try again","red"))
        print()
        continue
while True:
    try:
        print()
        print("\033[?25h",end='')
        print("\033[0m",end='')
        secs_user = input("Input your seconds> ")
        secs_user = int(secs_user)
        break
    except ValueError:
        print()
        print(Color.colorchng("Error! Please try again","red"))
        continue

total_secs = min_user * 60 +  secs_user

clock(total_secs)

