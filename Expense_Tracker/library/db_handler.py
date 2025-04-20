import sqlite3

DB_PATH = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        username TEXT NOT NULL,
        date TEXT DEFAULT CURRENT_DATE
    )""")
    conn.commit()
    conn.close()

def add_expense(name, category, amount, username):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (name, category, amount, username, date)
        VALUES (?, ?, ?, ?, DATE('now'))
    """, (name, category, amount, username))
    conn.commit()
    conn.close()

def get_expenses(username=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    if username:
        cursor.execute("SELECT * FROM expenses WHERE username = ?", (username,))
    else:
        cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_expense(expense_id, name, category, amount):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE expenses
        SET name = ?, category = ?, amount = ?
        WHERE id = ?
    """, (name, category, amount, expense_id))
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

def clear_expenses(username: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE username = ?", (username,))
    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM expenses")
    if cursor.fetchone()[0] == 0:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='expenses'")
        conn.commit()

    conn.close()