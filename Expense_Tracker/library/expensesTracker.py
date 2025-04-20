from library.expense import Expense
from library.db_handler import add_expense, get_expenses
from library.db_handler import clear_expenses as clear
import calendar
import datetime

DB_PATH = "expenses.db"

def save_expense(expense: Expense, username: str):
    add_expense(expense.name, expense.category, expense.amount, username)

def summarize_expenses(budget: float, username: str):
    rows = get_expenses(username)
    expenses = [
        Expense(name=row[1], category=row[2], amount=row[3])
        for row in rows
    ]

    amount_by_category = {}
    for expense in expenses:
        amount_by_category[expense.category] = amount_by_category.get(expense.category, 0) + expense.amount

    total_spend = sum(ex.amount for ex in expenses)
    remaining_budget = budget - total_spend

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    daily_budget = remaining_budget / remaining_days if remaining_days else 0

    return {
        'amount_by_category': amount_by_category,
        'total_spend': total_spend,
        'remaining_budget': remaining_budget,
        'daily_budget': daily_budget
    }

def clear_expenses(username: str):
    clear(username)
