import os 

class constants:
    def __init__(self):
        self.ICON = os.path.join('library','media','icon.ico') 
        self.BG = os.path.join('library','media','bg.jpg')
        self.WIDTH = 600
        self.HEIGHT = 400
        self.CURRENT_USER = None
        
constants = constants()