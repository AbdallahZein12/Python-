import tkinter as tk
from tkinter import messagebox, ttk
from constants import constants
from PIL import Image, ImageTk
from library.util import render_image, hash_password, dump_user, retrieve_users, check_password
from library.expensesTracker import summarize_expenses, save_expense, clear_expenses
from library.db_handler import update_expense, get_expenses
from library.expense import Expense
import matplotlib.pyplot as plt


class MainFrame(tk.Frame):
    def __init__(self, parent, bg="", width=constants.WIDTH, height=constants.HEIGHT):
        super().__init__(parent)
        self.parent = parent
        self.config(bg=bg, width=width, height=height)
        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()

        self.bg_image = render_image(constants.BG, width, height)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image)
        self.canvas.create_text(width // 2, 70, text="Expense Tracker!", font=("Bauhaus 93", 30), fill="white", anchor="center")
        self.canvas.create_text(width // 2, 130, text="Login or Register", font=("Arial", 20), fill="white", anchor="center")

        self.user_entry = tk.Entry(self, width=80)
        self.user_entry.insert(0, "Username")
        self.user_entry.bind('<FocusIn>', self.on_user_entry_click)
        self.user_entry.place(relx=0.5, rely=0.5, anchor='center')

        self.password_entry = tk.Entry(self, width=80, show='*')
        self.password_entry.insert(0, "Password")
        self.password_entry.bind('<FocusIn>', self.on_password_entry_click)
        self.password_entry.place(relx=0.5, rely=0.6, anchor='center')

        self.login_button = tk.Button(self, text="Login", width=20, command=self.login)
        self.login_button.place(relx=0.3, rely=0.8, anchor='center')

        self.register_button = tk.Button(self, text="Register", width=20, command=self.register)
        self.register_button.place(relx=0.7, rely=0.8, anchor='center')

        self.show_password_var = tk.IntVar(value=0)
        self.show_password_button = tk.Checkbutton(self, text="Show Pass", variable=self.show_password_var, command=self.check_password_show)
        self.show_password_button.place(relx=0.5, rely=0.8, anchor='center')

    def on_user_entry_click(self, event):
        if self.user_entry.get() == 'Username':
            self.user_entry.delete(0, tk.END)

    def on_password_entry_click(self, event):
        if self.password_entry.get() == 'Password':
            self.password_entry.delete(0, tk.END)

    def check_password_show(self):
        if self.show_password_var.get() == 1:
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def register(self):
        if not all([self.user_entry.get(), self.password_entry.get()]) or (self.user_entry.get() == 'Username' or self.password_entry.get() == 'Password'):
            messagebox.showinfo(title="An error has occured!", message='No input found')
            return
        users = retrieve_users()
        if self.user_entry.get() in users:
            messagebox.showinfo(title='User already exists!', message='User already exists!')
            return

        hashed_pass = hash_password(self.password_entry.get())
        data = (self.user_entry.get(), hashed_pass)
        dump_user(data)
        messagebox.showinfo(title='Success!', message='User created!')

    def login(self):
        users = retrieve_users()
        user, password = self.user_entry.get(), self.password_entry.get()
        if user in users:
            if check_password(password, users[user]):
                constants.CURRENT_USER = user
                self.parent.show_frame(self.parent.main_menu, fetch=True)
            else:
                messagebox.showinfo(title='Incorrect Password', message='The password is incorrect!')
        else:
            messagebox.showinfo(title='No user found', message='no user found!')


class MainMenu(tk.Frame):
    def __init__(self, parent, bg="", width=constants.WIDTH, height=constants.HEIGHT):
        super().__init__(parent)
        self.config(bg=bg, width=width, height=height)
        self.parent = parent

        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()
        self.bg_image = render_image(constants.BG, WIDTH=width, HEIGHT=height)
        self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image)

        self.bud_entry = tk.Entry(self, width=80)
        self.bud_entry.insert(0, "0")
        self.canvas.create_text(88, 70, text="Budget", font=("Arial", 15), fill="white")
        self.bud_entry.place(relx=0.5, rely=0.25, anchor='center')
        self.calculate_btn = tk.Button(self, text="Calculate", width=10, command=self.calculate)
        self.calculate_btn.place(relx=0.5, rely=0.32, anchor='center')

        self.expense_name_entry = tk.Entry(self, width=20)
        self.expense_name_entry.insert(0, "Expense")
        self.expense_name_entry.bind("<FocusIn>", lambda event: self.expense_name_entry.delete(0, tk.END) if self.expense_name_entry.get() == "Expense" else None)
        self.expense_name_entry.bind("<FocusOut>", lambda event: self.expense_name_entry.insert(0, "Expense") if self.expense_name_entry.get() == "" else None)
        self.expense_name_entry.place(relx=0.2, rely=0.40, anchor='center')

        self.expense_amount_entry = tk.Spinbox(self, from_=0, to=10000, increment=1, width=18)
        self.expense_amount_entry.place(relx=0.4, rely=0.40, anchor='center')

        self.expense_cat_entry = ttk.Combobox(self, values=["Marketing", "Product", "ShippingCost"], state="readonly", width=18)
        self.expense_cat_entry.set("Category")
        self.expense_cat_entry.place(relx=0.6, rely=0.40, anchor='center')

        self.expense_id_entry = tk.Entry(self, width=20)
        self.expense_id_entry.insert(0, "Expense ID")
        self.expense_id_entry.bind("<FocusIn>", lambda e: self.expense_id_entry.delete(0, tk.END) if self.expense_id_entry.get() == "Expense ID" else None)
        self.expense_id_entry.place(relx=0.6, rely=0.48, anchor='center')

        self.add_expense_btn = tk.Button(self, text='Add Expense', width=10, command=self.add_expense)
        self.add_expense_btn.place(relx=0.8, rely=0.40, anchor='center')

        self.update_expense_btn = tk.Button(self, text='Update Expense', width=12, command=self.update_expense_cmd)
        self.update_expense_btn.place(relx=0.8, rely=0.70, anchor='center')

        self.clear_expenses_btn = tk.Button(self, text='Clear All', width=10, command=self.clear_expenses_cmd)
        self.clear_expenses_btn.place(relx=0.8, rely=0.50, anchor='center')

        self.show_expenses_btn = tk.Button(self, text='Show Expense', width=12, command=self.expenselist_cmd)
        self.show_expenses_btn.place(relx=0.8, rely=0.8, anchor='center')

        self.plot_btn = tk.Button(self, text='Plot', width=10, command=self.plot)
        self.plot_btn.place(relx=0.8, rely=0.60, anchor='center')

    def calculate(self):
        try:
            budget = float(self.bud_entry.get())
        except Exception:
            messagebox.showinfo(title='Error!', message='Entry must be a number!')
            return
        
        self.values = summarize_expenses(budget=budget, username=constants.CURRENT_USER)

        self.update_values(self.values)

    def add_expense(self):
        try:
            budget = float(self.bud_entry.get())
            if budget == 0:
                messagebox.showinfo(title="No Budget Set", message="Please enter your budget before adding expenses.")
                return
        except ValueError:
            messagebox.showinfo(title="Invalid Budget", message="Please enter a valid numeric budget before adding expenses.")
            return
    
        if not all([self.expense_name_entry.get(), self.expense_cat_entry.get(), self.expense_amount_entry.get()]):
            messagebox.showinfo(title="Missing Fields!", message="All inputs must be filled!")
            return
        expense_cat = self.expense_cat_entry.get()
        if expense_cat not in ['Marketing', 'Product', 'ShippingCost']:
            messagebox.showinfo(title='Not a valid category!', message='Must be "Marketing", "Product", or "ShippingCost"')
            return
        try:
            expense_amount = float(self.expense_amount_entry.get())
            if expense_amount == 0:
                messagebox.showinfo(title='Invalid Amount', message='Amount must be greater than zero.')
                return
        except Exception:
            messagebox.showinfo(title='Incorrect format!', message='Amount must be a number!')
            return

        expense_name = self.expense_name_entry.get()
        expense = Expense(name=expense_name, category=expense_cat, amount=expense_amount)
        save_expense(expense=expense, username=constants.CURRENT_USER)
        self.calculate()

    def update_expense_cmd(self):
        try:
            expense_id = int(self.expense_id_entry.get())
            expense_name = self.expense_name_entry.get()
            expense_amount = float(self.expense_amount_entry.get())
            expense_cat = self.expense_cat_entry.get()

            if not expense_name or expense_cat not in ["Marketing", "Product", "ShippingCost"]:
                messagebox.showinfo(title="Invalid Data", message="Check all fields and try again.")
                return
            
            user_expenses = get_expenses(constants.CURRENT_USER)
            id_exists = any(exp[0] == expense_id for exp in user_expenses)

            if not id_exists:
                messagebox.showinfo(title="Invalid ID", message=f"No expense with ID {expense_id} found.")
                return

            update_expense(expense_id, expense_name, expense_cat, expense_amount)
            messagebox.showinfo(title="Success", message=f"Expense #{expense_id} updated successfully.")
            self.calculate()
        except ValueError:
            messagebox.showinfo(title="Error", message="Expense ID and amount must be numeric.")

    def expenselist_cmd(self):

        rows = get_expenses(constants.CURRENT_USER)
        if not rows:
            messagebox.showinfo("No Records", "You have no expenses logged.")
            return

        popup = tk.Toplevel(self)
        popup.title("Expense List")
        popup.geometry("650x400")
        popup.grab_set()  

        text_widget = tk.Text(popup, font=('Courier New', 10), padx=10, pady=10)
        text_widget.pack(fill=tk.BOTH, expand=True)

        header = f"{'ID':<5}{'Name':<20}{'Category':<15}{'Amount':<10}{'Date':<15}\n"
        separator = "-" * 65 + "\n"
        text_widget.insert(tk.END, header)
        text_widget.insert(tk.END, separator)

        for row in rows:
            id_, name, category, amount, _, date = row
            line = f"{id_:<5}{name:<20}{category:<15}${amount:<9.2f}{date:<15}\n"
            text_widget.insert(tk.END, line)

        text_widget.config(state=tk.DISABLED)

    def update_values(self, values):
        amounts = values['amount_by_category']
        self.marketing_amt.config(text=amounts.get("Marketing", 0.0))
        self.product_amt.config(text=amounts.get("Product", 0.0))
        self.shippingCost_amt.config(text=amounts.get("ShippingCost", 0.0))

        self.tot_spend_amt.config(text=f"{self.values['total_spend']:.2f}")
        self.remaining_bud_amt.config(text=f"{self.values['remaining_budget']:.2f}")
        self.daily_bud_lab_amt.config(text=f"{self.values['daily_budget']:.2f}")

    def clear_expenses_cmd(self):
        clear_expenses(username=constants.CURRENT_USER)
        self.calculate()

    def fetch_values(self):
        budget = int(self.bud_entry.get())
        self.canvas.create_text(290, 50, text=constants.CURRENT_USER, font=("Arial", 20), fill='white')
        self.values = summarize_expenses(budget=budget, username=constants.CURRENT_USER)

        self.amt_by_cat_lab = tk.Label(self, text='Amount by Category', font=('Arial', 10))
        self.amt_by_cat_lab.place(relx=0.08, rely=0.5)

        self.marketing_lab = tk.Label(self, text=f'Marketing', font=('Arial', 10))
        self.marketing_lab.place(relx=0.08, rely=0.6)

        self.product_lab = tk.Label(self, text=f'Product', font=('Arial', 10))
        self.product_lab.place(relx=0.08, rely=0.7)

        self.shippingCost_lab = tk.Label(self, text=f'ShippingCost', font=('Arial', 10))
        self.shippingCost_lab.place(relx=0.08, rely=0.8)

        self.marketing_amt = tk.Label(self, font=('Arial', 10))
        self.marketing_amt.place(relx=0.25, rely=0.6)

        self.product_amt = tk.Label(self, font=('Arial', 10))
        self.product_amt.place(relx=0.25, rely=0.7)

        self.shippingCost_amt = tk.Label(self, font=('Arial', 10))
        self.shippingCost_amt.place(relx=0.25, rely=0.8)

        self.tot_spend_lab = tk.Label(self, text=f'Total Spend', font=('Arial', 10))
        self.tot_spend_lab.place(relx=0.35, rely=0.6)

        self.remaining_bud_lab = tk.Label(self, text=f'Remaining Budget', font=('Arial', 10))
        self.remaining_bud_lab.place(relx=0.35, rely=0.7)

        self.daily_bud_lab = tk.Label(self, text=f'Daily Budget', font=('Arial', 10))
        self.daily_bud_lab.place(relx=0.35, rely=0.8)

        self.tot_spend_amt = tk.Label(self, text=self.values['total_spend'], font=('Arial', 10))
        self.tot_spend_amt.place(relx=0.55, rely=0.6)

        self.remaining_bud_amt = tk.Label(self, text=self.values['remaining_budget'], font=('Arial', 10))
        self.remaining_bud_amt.place(relx=0.55, rely=0.7)

        self.daily_bud_lab_amt = tk.Label(self, text=self.values['daily_budget'], font=('Arial', 10))
        self.daily_bud_lab_amt.place(relx=0.55, rely=0.8)

        self.update_values(self.values)


    def plot(self):
        try:
            budget = float(self.bud_entry.get())
        except Exception:
            messagebox.showinfo(title='Error!', message='Budget Entry must be a number!')
            return
        self.values = summarize_expenses(budget=budget, username=constants.CURRENT_USER)

        categories = list(self.values['amount_by_category'].keys())
        spending = list(self.values['amount_by_category'].values())
        cats_spending = list(zip(categories, spending))

        labs = [f'{i[0]} = {i[1]}' for i in cats_spending]
        handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in ['blue', 'green', 'purple']]
        fig = plt.figure(figsize=(8, 4))
        plt.bar(categories, spending, color=['blue', 'green', 'purple'])
        plt.title('Category Spending')
        plt.ylabel('Amount ($)')
        plt.xlabel('Categories')
        plt.ylim(0, self.values['total_spend'])
        plt.legend(labels=labs, handles=handles)
        plt.show()

        if self.values['remaining_budget'] > 0:
            labels = ['Total Spend', 'Remaining Budget']
            sizes = [self.values['total_spend'], self.values['remaining_budget']]
            colors = ['green', 'orange']

            plt.figure(figsize=(6, 6))
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
            plt.title('Budget Distribution', y=1.1)
            plt.axis('equal')
        plt.show()
