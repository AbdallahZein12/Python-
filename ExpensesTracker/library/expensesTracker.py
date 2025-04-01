from library.expense import Expense
import calendar
import datetime
import os 



#Add a password and user name system at the very beggening of the program
#Add a chart
#Design: Add GUI for better desing and looking
# def main():
#    print(f" Running Expense Tracker !")
#    expense_file_path = os.path.join('output','expenses.csv')
#    budget = float(input(" Enter your budget:"))
  
  
#    # Get user to input his expense
#    expense = get_user_expense()


#    # Write their expense to a file
#    save_expense_to_file(expense, expense_file_path)


#    # Read file and summarize their expense
#    summarize_expenses(expense_file_path, budget)


# def get_user_expense(expense_name,expense_amount,expense_category):
#    print(f" Getting User Expense")
#    expense_name = input(" Enter expense name:")
#    expense_amount = float(input("Enter expense amount:"))
#    print(f" Your Expense is:{expense_name}, ${expense_amount}")
#    expense_category = [
#        "  Marketing",
#        "  Product",
#        "  ShippingCost",
#        ]
  
#    while True:
#        print("Select a category:")
#        for i, category_name in enumerate(expense_category):
#            print(f"  {i + 1}. {category_name}")


#        value_range = f"[0 - {len(expense_category)}]"
#        selected_index = int(input(f' Enter a category number {value_range}: '))
      
    #    if selected_index in range(len(expense_category)+1):
    #        selected_category = expense_category[selected_index-1]
    #        new_expense = Expense(
    #            name=expense_name, category=selected_category, amount=expense_amount
    #            )
    #        return new_expense
    #    else:
    #        print('Invalid Category. Please try again!')


    #    break
  


def save_expense_to_file(expense: Expense, expense_file_path):
#    print(f" Saving User Expense: {expense} to {expense_file_path}")
   if os.path.exists(expense_file_path):
       mode = 'a'
   else:
       mode = 'w'
   with open(expense_file_path, mode) as f:
       f.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize_expenses(expense_file_path, budget):
    #    print(f" Summarizing User Expenses")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
       lines = f.readlines()
       for line in lines:
           expense_name, expense_category, expense_amount = line.strip().split(",")
           line_expense = Expense(
               name=expense_name.title(),
               category=expense_category.title(),
               amount=float(expense_amount)
           )
           expenses.append(line_expense)
  
    amount_by_category = {}
    for expense in expenses:
        amount_by_category[expense.category] = amount_by_category.get(expense.category,0) + expense.amount
        #    key = expense.category
        #    if key in amount_by_category:
        #        amount_by_category[key] += expense.amount
        #    else:
        #        amount_by_category[key] = expense.amount
    
        #    print("Expenses By Category :")
        #    for key, amount in amount_by_category.items():
        #        print(f"  {key}: ${amount:.2f}")


    total_spend = sum([ex.amount for ex in expenses])
        #    print(f" You've spent ${total_spend:.2f}")


    remaining_budget = budget - total_spend
        #    print(green(f" Budget Remaining: ${remaining_budget:.2f}"))



    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day


    daily_budget = remaining_budget / remaining_days if remaining_days else 1
        #    print(green(f" Budget Per Day: ${daily_budget:.2f}"))

    return {'amount_by_category':amount_by_category,
            'total_spend':total_spend,
            'remaining_budget':remaining_budget,
            'daily_budget':daily_budget}

def clear_expenses(file_path):
    with open(file_path,'w') as f:
        pass
    marketing_expense = Expense(name="..",category="Marketing",amount="0")
    product_expense = Expense(name="..",category="Product",amount="0")
    shippingcost_expense = Expense(name="..",category="Shippingcost",amount="0")
    save_expense_to_file(marketing_expense,file_path)
    save_expense_to_file(product_expense,file_path)
    save_expense_to_file(shippingcost_expense,file_path)
    