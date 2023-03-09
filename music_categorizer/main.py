import time, os, sys, csv, random  
from getpass import getpass
from PIL import Image
import shutil, ast

colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m"
}

class Color: 
    @staticmethod
    def chg_col(str,color_choice):
        if color_choice.lower().strip() in colors:
            return f"{colors[color_choice]}{str}\033[0m"

class Loading: 
    def __init__(self, string,time):
        self.time = time
        self.string = string
        
class Stringer(Loading):
    def __init__(self,string,time):
        super().__init__(string,time)
    
    def stringer(self):
        for i in self.string:
            print(random.choice(list(colors.values())),i,"\033[0m",end='',sep='')
            sys.stdout.flush()
            time.sleep(self.time)
            
class Billboard(Loading):
    def __init__(self,string,time,colors):
        super().__init__(string,time)
        self.colors = colors
        
    def billboard(self):
        if self.colors == True:
            count = 0
            while True:
                for i in self.string:
                    print(random.choice(list(colors.values())),i,"\033[0m",end='',sep='')
                    sys.stdout.flush()
                print()
                sys.stdout.write("\033[F")
                count += 1
                if count == self.time:
                    break
                else:
                    continue
        else: 
            count = 0
            while True:
                for i in self.string:
                    print(i,end='',sep='')
                    sys.stdout.flush()
                    time.sleep(0.3)
                print('\b\b\b   \b\b\b',end='')
                count += 1
                if count == self.time:
                    break
                else:
                    continue
            
            
def space(spc):
    x = ""
    print(f"{x:{spc}}",end='')

def home():
    os.system('cls')
    print("\033[31m",end='')
    print("\033[?25l",end='')
    with Image.open('logo.png') as im:
        im = im.convert('L')
        im = im.resize((100,20))
        chars = '.:-=+*#%@'
        for y in range(im.size[1]):
            time.sleep(0.05)
            for x in range(im.size[0]):
                gray = im.getpixel((x,y))
                char = chars[gray * len(chars) // 355]
                
                print(char,end='')
            print()
    
    print("""
          --------------------------------------------------------------- 
          |                                                             |
          |                                                             |
          """)
    
    space("<35")
    welcome_page = Stringer("WELCOME", 0.1)
    welcome_page.stringer()
    print("\033[31m",end='')
            
    print("""
          |                                                             | 
          |                                                             |
          """)
    
    print("\033[31m")
    getpass("                          Press enter to continue!")
    print()
    
    try:
        f = open("100MostStreamedSongs.csv", 'r')
        f.close()
    except Exception as er:
        os.system('cls')
        print(Color.chg_col("Error! exiting program","red"))
        print()
        print(er)
        time.sleep(1)
        print()
        print("Exiting",end='')
        
        loading_dots = Billboard("...", 5, False)
        loading_dots.billboard()
        
        exit()
    
    if os.path.exists("Results!") == False:
        os.mkdir("Results!")
    else: 
        shutil.rmtree("D:\Code\python_projects\music_categorizer\Results!")
        os.mkdir("Results!")
    
    with open("100MostStreamedSongs.csv","r", encoding='utf-8') as f:
      
        
        parent_dir = "D:\Code\python_projects\music_categorizer\Results!"
        artists = []
        
        reader = csv.DictReader(f)
        for row in reader:
            if row["Artist(s)"] in artists:
                path = os.path.join(fr"D:\Code\python_projects\music_categorizer\Results!\{row['Artist(s)']}",f"{row['Song']}")
              
                # path = path.replace("\xa0", " ")
                # # path = path.replace("\\",ast.literal_eval("\\"))
                
                # path = path.replace("\\\\","\\")
                # path =  '"' + ast.literal_eval(path) + '"'
                with open(path, 'w') as w:
                    w.write(f"Rank: {row['Rank']}\nDate: {row['Date published']}\nStreams: {row['Streams']}")
            else:
                artists.append(row["Artist(s)"])
                path = os.path.join(parent_dir, row["Artist(s)"])
                os.mkdir(path)
                path = os.path.join(fr"D:\Code\python_projects\music_categorizer\Results!\{row['Artist(s)']}",f"{row['Song']}")
             
                # path = path.replace("\xa0", " ")
                # # path = path.replace("\\",ast.literal_eval("\\"))
                
                # path = path.replace("\\\\","\\")
                # # path = '"' + ast.literal_eval(path) + '"'
                with open(path, 'w') as w:
                    w.write(f"Rank: {row['Rank']}\nDate: {row['Date published']}\nStreams: {row['Streams']}")

        
        os.system('cls')
        print("Loading",end='')
        loading_dots = Billboard("...", 5, False)
        loading_dots.billboard()
        time.sleep(0.2)
        os.system('cls')
        print()
        space("<15")
        print("COMPLETE")
        



                
          
    
home()

            





        
        
        