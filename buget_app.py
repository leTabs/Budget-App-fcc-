class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        # creating the deposit method 

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
        # creating the withdraw method

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
        # creating the balance method 

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False
        # creating the transfer method

    def check_funds(self, amount):
        return amount <= self.get_balance()
        # creating the check_funds method

    def __str__(self):
        title = "*" * ((30 - len(self.name)) // 2) + self.name + "*" * ((30 - len(self.name)) // 2)
        if len(title) < 30:
            title += "*"
        items = ""
        for item in self.ledger:
            items += item["description"][:23].ljust(23) + "{:.2f}".format(item["amount"]).rjust(7) + "\n"
        total = "Total: {:.2f}".format(self.get_balance())
        return title + "\n" + items + total
        # format the string representation of the class
        
        
def create_spend_chart(categories):
    withdrawals = []
    names = []
    # will be used later
    
    for category in categories:
        withdrawals.append(0)
        for item in category.ledger:
            if item["amount"] < 0:
                withdrawals[-1] += abs(item["amount"])
        names.append(category.name)
        # append the widthrawls at a stand-by state and the name to the respective lists

    withdrawals_total = sum(withdrawals)
    # calculate the total amount of the withdrawals
    withdrawals_percentage = []
    for withdrawal in withdrawals:
        percentage = withdrawal / withdrawals_total * 100
        withdrawals_percentage.append(int(percentage // 10) * 10)
        # calculate and append the percentages in the withdrawals_percentage list
        
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in withdrawals_percentage:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    # format the chart accordingly
    
    max_name_length = max([len(name) for name in names])
    for i in range(max_name_length):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"
    # include the names of each category to the chart 
    return chart
