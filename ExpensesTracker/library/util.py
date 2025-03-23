from PIL import Image, ImageTk
import json 
import ctypes
import os 
import bcrypt
import base64
import sqlite3

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


def retrieve_users(file_path='creds.db'):
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    users = {i[0]:i[1] for i in users}
    return users 

def dump_user(data,file_path='creds.db'):
    conn = sqlite3.connect(file_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (data[0], data[1]))
    conn.commit()
    conn.close()
                
          
    
    