import pytest
from library.expense import Expense
from library.expensesTracker import save_expense, summarize_expenses, clear_expenses

@pytest.fixture(autouse=True)
def setup_function():
    clear_expenses("testuser")

def test_summarize_expenses():
    save_expense(Expense("Item1", "Product", 20.0), "testuser")
    save_expense(Expense("Item2", "Marketing", 30.0), "testuser")
    summary = summarize_expenses(budget=100.0, username="testuser")
    assert summary['total_spend'] == 50.0
    assert summary['remaining_budget'] == 50.0
    assert summary['amount_by_category']["Product"] == 20.0
    assert summary['amount_by_category']["Marketing"] == 30.0

def test_daily_budget_calculation():
    save_expense(Expense("Item1", "Product", 60.0), "testuser")
    summary = summarize_expenses(budget=120.0, username="testuser")

    assert summary['daily_budget'] >= 0

def test_empty_expense_summary():
    summary = summarize_expenses(budget=80.0, username="testuser")

    assert summary['total_spend'] == 0.0
    assert summary['remaining_budget'] == 80.0
    assert summary['amount_by_category'] == {}