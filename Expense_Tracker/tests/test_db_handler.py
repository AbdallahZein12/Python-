import sqlite3
from library.db_handler import init_db, add_expense, get_expenses, update_expense, delete_expense, clear_expenses

def setup_function():
    init_db()
    clear_expenses("testuser")

def test_add_and_get_expense():
    add_expense("Lunch", "Product", 15.0, "testuser")
    expenses = get_expenses("testuser")
    assert len(expenses) == 1
    assert expenses[0][1] == "Lunch"

def test_update_expense():
    add_expense("Lunch", "Product", 15.0, "testuser")
    expense_id = get_expenses("testuser")[0][0]
    update_expense(expense_id, "Dinner", "Marketing", 25.0)
    updated = get_expenses("testuser")[0]
    assert updated[1] == "Dinner"
    assert updated[2] == "Marketing"

def test_delete_expense():
    add_expense("Lunch", "Product", 15.0, "testuser")
    expense_id = get_expenses("testuser")[0][0]
    delete_expense(expense_id)
    assert len(get_expenses("testuser")) == 0