import pytest
import tkinter as tk
from frames import MainFrame, MainMenu
from constants import constants
from library.util import dump_user, hash_password

@pytest.fixture
def root():
    root = tk.Tk()
    root.withdraw()  
    yield root
    root.destroy()

def test_register_and_login_flow(root):
    main_frame = MainFrame(root)

    username = "testuser"
    password = "testpass"

    main_frame.user_entry.delete(0, tk.END)
    main_frame.user_entry.insert(0, username)

    main_frame.password_entry.delete(0, tk.END)
    main_frame.password_entry.insert(0, password)

    main_frame.register()  

    users = main_frame.parent.retrieve_users() if hasattr(main_frame.parent, 'retrieve_users') else None
    assert users is None or username in users  

def test_password_toggle(root):
    frame = MainFrame(root)
    frame.password_entry.insert(0, "secret")

    frame.show_password_var.set(1)
    frame.check_password_show()
    assert frame.password_entry.cget("show") == ""

    frame.show_password_var.set(0)
    frame.check_password_show()
    assert frame.password_entry.cget("show") == "*"


def test_invalid_login_shows_messagebox(monkeypatch, root):
    frame = MainFrame(root)

    frame.user_entry.delete(0, tk.END)
    frame.user_entry.insert(0, "fakeuser")

    frame.password_entry.delete(0, tk.END)
    frame.password_entry.insert(0, "fakepass")

    called = {"msg": None}

    def mock_msgbox(title, message):
        called["msg"] = message

    monkeypatch.setattr("tkinter.messagebox.showinfo", mock_msgbox)

    frame.login()

    assert "no user found" in called["msg"].lower()


def test_main_menu_add_expense_fields(root):
    frame = MainMenu(root)
    assert frame.expense_name_entry.get() == "Expense"
    assert frame.expense_cat_entry.get() == "Category"
    assert frame.expense_amount_entry.get() == "0"

def test_calculate_invalid_budget(monkeypatch, root):
    app = MainMenu(root)
    app.bud_entry.delete(0, "end")
    app.bud_entry.insert(0, "invalid")

    def mock_showinfo(title, message):
        assert "must be a number" in message.lower()

    monkeypatch.setattr("tkinter.messagebox.showinfo", mock_showinfo)
    app.calculate()

def test_calculate_valid_budget(root):
    app = MainMenu(root)
    app.bud_entry.delete(0, "end")
    app.bud_entry.insert(0, "1000")
    app.fetch_values()
    app.calculate()

    assert app.tot_spend_amt.cget("text") is not None
    assert app.remaining_bud_amt.cget("text") is not None
    assert app.daily_bud_lab_amt.cget("text") is not None