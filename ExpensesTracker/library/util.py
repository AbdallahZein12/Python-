from PIL import Image, ImageTk
import json 
import ctypes
import os 
import bcrypt
import base64

class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name 
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"


def render_image(path,WIDTH,HEIGHT):
    opened_bg = Image.open(path)
    opened_bg = opened_bg.resize((WIDTH,HEIGHT),Image.LANCZOS)
    tk_bg = ImageTk.PhotoImage(opened_bg)
    return tk_bg

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'),salt=salt)
    hashed_pass_str = base64.b64encode(hashed_pass).decode('utf-8')
    return hashed_pass_str

def check_password(password,hashed_pw):
    hashed_pw = base64.b64decode(hashed_pw)
    return bcrypt.checkpw(password.encode('utf-8'),hashed_pw)


def retrieve_users(file_path='creds.json'):
    if os.path.exists(file_path):
        with open(file_path,'r') as f:
            try:
                d = json.load(f)
                if not isinstance(d,dict):
                    d = {}
            except json.JSONDecodeError:
                d = {}
        return d 
    else:
        return {}

def dump_user(data,file_path = 'creds.json'):
    # with open('creds.json','w') as f:
    #     json.dump(data,f,indent=4)
    
    if not os.path.exists('creds.json'):
        with open(file_path,'w') as f:
            json.dump({data[0]:data[1]},f, indent=4)
        # if os.name == 'nt':
        #     os.chmod(file_path, 0o666)
        #     FILE_ATTRIBUTE_HIDDEN = 0x02
        #     ctypes.windll.kernel32.SetFileAttributesW('creds.json',FILE_ATTRIBUTE_HIDDEN)
        # else:
        #     hidden_path = os.path.join('.','creds.json')
        #     os.rename('creds.json',hidden_path)
        return 
    
    d = retrieve_users()
    
    d[data[0]] = data[1]
    
    with open(file_path,'w') as f:
        json.dump(d,f,indent=4)
                
          
    
    