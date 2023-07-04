class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.funds = 0.0

  def __repr__(self):
    header = self.category.center(30,"*") + "\n"
    ledger = ""
    for i in self.ledger:
      line_descri = f"{i['description'][:23]}"
      line_amount = "{:>7.2f}".format(i['amount'])
      line_amount = line_amount[:7]
      ledger += f"{line_descri}{line_amount}\n"
    total = "Total: {:.2f}".format(self.funds)
    return header + ledger + total

  def check_funds(self,amount):
    if amount > self.funds:
      return False
    else:
      return True
    
  def deposit(self, amount, descri=""):
    self.ledger.append({"amount": amount, "description": descri})
    self.funds += amount
    
  def withdraw(self, amount, descri=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": (-1 * amount), "description": descri})
      self.funds -= amount
      return True
    else:
      return False

  def get_balance(self):
    return self.funds

  def transfer(self, amount, category):
    if self.withdraw(amount=amount, descri=f"Transfer to {category}"):
      category.deposit(amount=amount,descri=f"Transfer from {category}")
      return True
    else:
      return False

  
    
    
def create_spend_chart(categories):
  spent_amounts = []
  for i in categories:
    spent = 0
    for item in i.ledger:
      if item["amount"] < 0:
        spent += abs(item["amount"])
    spent_amounts.append(round(spent,2))


  total = round(sum(spent_amounts),2)
  spent_percentage = list(map(lambda amount: int(((amount / total) * 100) // 1), spent_amounts))

  header = "Percentage spent by category\n"

  chart = ""
  for i in reversed(range(0,101,10)):
    chart += str(i).rjust(3) + "|"
    for percent in spent_percentage:
      if percent >= i:
        chart += " o "
      else:
        chart += "   "

    chart += "\n"

  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
  descriptions = list(map(lambda category: category.category ,categories))
  max_length = max(map(lambda description: len(description), descriptions))
  descriptions = list(map(lambda description: description.ljust(max_length), descriptions))

  for x in zip(*descriptions):
    footer += "    " + "".join(map(lambda s: s.center(3),x))

  return (header + chart + footer).rstrip("\n")
    
    
    