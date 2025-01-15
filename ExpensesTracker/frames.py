import tkinter as tk
from tkinter import messagebox,ttk
from constants import constants
from PIL import Image,ImageTk
from library.util import render_image, hash_password, dump_user,retrieve_users, check_password
import time 
import os 
from library.expensesTracker import summarize_expenses,save_expense_to_file,clear_expenses
from library.expense import Expense
import matplotlib.pyplot as plt 


class MainFrame(tk.Frame):
    def __init__(self, parent, bg="", width=constants.WIDTH, height=constants.HEIGHT):
        super().__init__(parent)
        self.parent = parent
        self.config(bg=bg, width=width, height=height)
        self.canvas = tk.Canvas(self,width=width,height=height)
        self.canvas.pack()

        self.bg_image = render_image(constants.BG,width,height)
        self.canvas.create_image(0,0,anchor='nw',image=self.bg_image)
        self.canvas.create_text(290,50,text="Expenses Tracker!", font=("Bauhaus 93", 20),fill="brown")
        self.canvas.create_text(300,130,text="Login or Register",font=("Arial", 20),fill='brown')

        self.user_entry = tk.Entry(self,width=80)
        self.user_entry.insert(0,"Username")
        self.user_entry.bind('<FocusIn>',self.on_user_entry_click)
        self.user_entry.place(relx=0.5,rely=0.5,anchor='center')
        
        self.password_entry = tk.Entry(self,width=80,show='*')
        self.password_entry.insert(0,"Password")
        self.password_entry.bind('<FocusIn>', self.on_password_entry_click)
        self.password_entry.place(relx=0.5,rely=0.6, anchor='center')
        
        self.login_button = tk.Button(self, text="Login",width=20,command=self.login)
        self.login_button.place(relx=0.3,rely=0.8,anchor='center')
        
        self.register_button = tk.Button(self, text="Register",width=20,command=self.register)
        self.register_button.place(relx=0.7,rely=0.8,anchor='center')
        
        self.show_password_var = tk.IntVar(value=0)
        self.show_password_button = tk.Checkbutton(self,text="Show Pass",variable=self.show_password_var,command=self.check_password_show)
        self.show_password_button.place(relx=0.5,rely=0.8,anchor='center')
        # self.button = tk.Button(self,text='click', command=self.on_button_click)
        # self.button.place(x=100,y=350)
        
    def on_user_entry_click(self,event):
        if self.user_entry.get() == 'Username':
            self.user_entry.delete(0,tk.END)
            
    def on_password_entry_click(self,event):
        if self.password_entry.get() == 'Password':
            self.password_entry.delete(0,tk.END)
            
    def check_password_show(self):
        if self.show_password_var.get() == 1:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
            
    def register(self):
        if not all([self.user_entry.get(),self.password_entry.get()]) or (self.user_entry.get() == 'Username' or self.password_entry.get() == 'Password'):
            messagebox.showinfo(title="An error has occured!",message='No input found')
            return
        users = retrieve_users()
        if self.user_entry.get() in users:
            messagebox.showinfo(title='User already exists!', message='User already exists!')
            return
        
        hashed_pass = hash_password(self.password_entry.get())
        data = (self.user_entry.get(),hashed_pass)
        dump_user(data)
        messagebox.showinfo(title='Success!',message='User created!')
        
    def login(self):
        users = retrieve_users()
        user, password = self.user_entry.get(), self.password_entry.get()
        if user in users:
            if check_password(password,users[user]):
                # messagebox.showinfo(title='Success!',message='LOGIN SUCCESSFUL!')
                constants.CURRENT_USER = user
                self.parent.show_frame(self.parent.main_menu,fetch=True)
                
            else:
                messagebox.showinfo(title='Incorrect Password', message='The password is incorrect!')
        else:
            messagebox.showinfo(title='No user found',message='no user found!')
            
   
        
        
    
        
class MainMenu(tk.Frame):
    def __init__(self, parent, bg="", width=constants.WIDTH, height=constants.HEIGHT):
        super().__init__(parent)
        self.config(bg=bg, width=width, height=height)
        self.parent = parent  
        
        # self.label = tk.Label(self, text='Test',font=('Arial',20))
        # self.label.place(x=300,y=100)
        
        self.canvas = tk.Canvas(self,width=width,height=height)
        self.canvas.pack()
        self.bg_image = render_image(constants.BG,WIDTH=width,HEIGHT=height)
        self.canvas.create_image(0,0,anchor='nw',image=self.bg_image)
        self.bud_entry = tk.Entry(self,width=80)
        self.bud_entry.insert(0,"0")
        self.canvas.create_text(100,70,text="Budget",font=("Arial",15))
        self.bud_entry.place(relx=0.5,rely=0.25,anchor='center')
        self.calculate_btn = tk.Button(self, text="Calculate",width=10,command=self.calculate)
        self.calculate_btn.place(relx=0.5,rely=0.32,anchor='center')
        
        self.expense_name_entry = tk.Entry(self,width=20)
        self.expense_name_entry.insert(0,"Expense")
        self.expense_name_entry.place(relx=0.2,rely=0.40,anchor='center')
        
        self.expense_amount_entry = tk.Entry(self,width=20)
        self.expense_amount_entry.insert(0,"0")
        self.expense_amount_entry.place(relx=0.4,rely=0.40,anchor='center')
        
        self.expense_cat_entry = tk.Entry(self,width=20)
        self.expense_cat_entry.insert(0,"Category")
        self.expense_cat_entry.place(relx=0.6,rely=0.40,anchor='center')
        
        self.add_expense_btn = tk.Button(self,text='Add Expense',width=10,command=self.add_expense)
        self.add_expense_btn.place(relx=0.8,rely=0.40,anchor='center')
        
        self.clear_expenses_btn = tk.Button(self,text='Clear Expenses',width=10,command=self.clear_expenses_cmd)
        self.clear_expenses_btn.place(relx=0.8,rely=0.50, anchor='center')
        
        self.plot_btn = tk.Button(self,text='Plot',width=10,command=self.plot)
        self.plot_btn.place(relx=0.8,rely=0.60, anchor='center')
        
    def calculate(self):
        try:
            budget = float(self.bud_entry.get())
        except Exception as e:
            messagebox.showinfo(title='Error!',message=f'Entry must be a number!')
            return
        self.values = summarize_expenses(expense_file_path=self.expenses,budget=budget)
            
        for i in self.values['amount_by_category']:
            placeholder = f'{i}_amount'
            val = getattr(self,placeholder)
            val.config(text=self.values['amount_by_category'][i])
        self.tot_spend_amt.config(text=self.values['total_spend'])
        self.remaining_bud_amt.config(text=self.values['remaining_budget'])
        self.daily_bud_lab_amt.config(text=self.values['daily_budget'])
        
    def add_expense(self):
        if not all([self.expense_name_entry.get(),self.expense_cat_entry.get(),self.expense_amount_entry.get()]):
            messagebox.showinfo(title="Missing Fields!",message="All inputs must be filled!")
            return 
        expense_cat = self.expense_cat_entry.get().title()
        if expense_cat not in ['Marketing','Product','Shippingcost']:
            messagebox.showinfo(title='Not a valid category!',message='Must be "Marketing", "Product", or "ShippingCost')
            return 
        try:
            expense_amount = float(self.expense_amount_entry.get())
        except Exception as e:
            messagebox.showinfo(title='Incorrect format!', message='Amount must be a number!')
            return 

        expense_name = self.expense_name_entry.get()
        expense = Expense(name=expense_name, category=expense_cat,amount=expense_amount)
        save_expense_to_file(expense=expense,expense_file_path=self.expenses)
        self.bud_entry.delete(0,tk.END)
        self.bud_entry.insert(0,"0")
        self.calculate()
    
    def clear_expenses_cmd(self):
        clear_expenses(self.expenses)
        self.calculate()
        
    

    def fetch_values(self):
        budget = int(self.bud_entry.get())
        self.canvas.create_text(290,50,text=constants.CURRENT_USER,font=("Arial",20),fill='brown')
        expenses = os.path.join('library','output',f'{constants.CURRENT_USER}.csv')
        self.expenses = expenses
        if not os.path.exists(expenses):
            
            marketing_expense = Expense(name="..",category="Marketing",amount="0")
            product_expense = Expense(name="..",category="Product",amount="0")
            shippingcost_expense = Expense(name="..",category="Shippingcost",amount="0")
            save_expense_to_file(marketing_expense,expenses)
            save_expense_to_file(product_expense,expenses)
            save_expense_to_file(shippingcost_expense,expenses)
                
                 
        # print(summarize_expenses(expense_file_path=expenses,budget=budget))
        self.values = summarize_expenses(expense_file_path=expenses, budget=budget)

        self.amt_by_cat_lab = tk.Label(self,text='Amount by Category',font=('Arial',10))
        self.amt_by_cat_lab.place(relx=0.08,rely=0.5)
        
        rely = 0.6
        for i in self.values['amount_by_category']:
            self.i = tk.Label(self,text=f'{i}',font=('Arial',10))
            self.i.place(relx=0.08,rely=rely)
            str_placeholder = f"{i}_amount"
            setattr(self, str_placeholder, tk.Label(self,text=self.values['amount_by_category'][i],font=('Arial',10)))
            val = getattr(self,str_placeholder)
            val.place(relx=0.25,rely=rely)
            rely+=0.1
            
        self.tot_spend_lab = tk.Label(self,text=f'Total Spend',font=('Arial',10))
        self.tot_spend_lab.place(relx=0.35,rely=0.6)
        
        self.remaining_bud_lab = tk.Label(self,text=f'Remaining Budget',font=('Arial',10))
        self.remaining_bud_lab.place(relx=0.35,rely=0.7)
        
        self.daily_bud_lab = tk.Label(self,text=f'Daily Budget',font=('Arial',10))
        self.daily_bud_lab.place(relx=0.35,rely=0.8)
        
        self.tot_spend_amt = tk.Label(self,text=self.values['total_spend'],font=('Arial',10))
        self.tot_spend_amt.place(relx=0.55,rely=0.6)
        
        self.remaining_bud_amt = tk.Label(self,text=self.values['remaining_budget'],font=('Arial',10))
        self.remaining_bud_amt.place(relx=0.55,rely=0.7)
        
        self.daily_bud_lab_amt = tk.Label(self,text=self.values['daily_budget'],font=('Arial',10))
        self.daily_bud_lab_amt.place(relx=0.55,rely=0.8)
    
    def plot(self):
        try:
            budget = float(self.bud_entry.get())
        except Exception as e:
            messagebox.showinfo(title='Error!',message=f'Budget Entry must be a number!')
            return
        self.values = summarize_expenses(expense_file_path=self.expenses,budget=budget)
    
        
        categories = list(self.values['amount_by_category'].keys())
        spending = list(self.values['amount_by_category'].values())
        cats_spending = list(zip(categories,spending))

        labs = [f'{i[0]} = {i[1]}' for i in cats_spending]
        handles = [plt.Rectangle((0,0),1,1, color=color) for color in ['blue','green','purple']]
        fig = plt.figure(figsize=(8,4))
        plt.bar(categories,spending,color=['blue','green','purple'])
        plt.title('Category Spending')
        plt.ylabel('Amount ($)')
        plt.xlabel('Categories')
        plt.ylim(0, self.values['total_spend'])
        plt.legend(labels=labs, handles=handles)
        plt.show()
        
        if self.values['remaining_budget'] > 0:
            
            labels = ['Total Spend','Remaining Budget']
            sizes = [self.values['total_spend'], self.values['remaining_budget']]
            colors=  ['green','orange']
        
            plt.figure(figsize=(6,6))
            plt.pie(sizes,labels=labels, autopct = '%1.1f%%',startangle=90, colors=colors)
            plt.title('Budget Distribution',y=1.1)
            plt.axis('equal')
        plt.show()
    
        
                     
        
        
        
            
        
        
    # def on_button_click(self):
    #     self.label.config(text='button clicked!')