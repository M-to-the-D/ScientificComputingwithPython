class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
    def __str__(self):
        title=f"{self.category_name:*^30}\n"
        items=''
        total=0
        for entry in self.ledger:
            amount=entry['amount']
            description=entry['description']
            items+=f"{description[:23]:23}{amount:>7.2f}\n"
            total+=amount
        op=title+items+'\n'+f'Total:{total:.2f}'
        return op
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    def get_balance(self):
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance
    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination_category.category_name}")
            destination_category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
    def get_withdraw(self):
        balance = 0
        for entry in self.ledger:
            if entry["amount"]<0:
                balance += entry["amount"]
        return balance

def create_spend_chart(categories):
    total_withdrawals, percentages=[],[]
    for category in categories:
        total_withdrawals.append(abs(category.get_withdraw()))
    i=0
    for category in categories:
        percentages.append((total_withdrawals[i] / sum(total_withdrawals)) * 100)
        i+=1
    chart = "Percentage spent by category\n"
    print(percentages, total_withdrawals)
    for percentage in range(100, -1, -10):
        chart += "{:>3}| ".format(percentage)
        for p in percentages:
            chart += "o  " if p > percentage else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Get the vertical category names
    category_names = [category.category_name for category in categories]
    max_name_length = max(len(name) for name in category_names)
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            chart += "{}  ".format(name[i] if i < len(name) else ' ')
        if i < max_name_length - 1:
            chart += "\n"
    return chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))