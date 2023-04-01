class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        self.withdraw_amount = 0

    def check_funds(self, amount):
        if amount < self.balance: return True
        else: return False

    def deposit(self,amount, description = ""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": - amount, "description": description})
            self.balance -= amount
            self.withdraw_amount += amount
            return True
        else: return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, d_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {d_category}")
            d_category.deposit(amount, f"Transfer from {self.category}")
            #print(d_category.category, self.category)
            return True
        else: return False

    def __str__(self):
        print('*************Food*************')
        #print(self.ledger)
        #print(self.ledger[0])
        for item in self.ledger:
            v =f"{item['amount']:.2f}"

            print(f"{item['description'][:23]:<23}{str(v)[:7]:>}")
        return f'Total: {self.get_balance()}'



f = Category('FOOD')
f.deposit(200, 'fist dep')
f.withdraw(23, 'pasta')
f.withdraw(45, 'restoraunt')
#print(f.get_balance())
#print(f)



#print(f.get_balance())
############################################################################
def create_spend_chart(categories):
    line = 5
    total = categories.withdraw_amount + categories.get_balance()
    percentage = (categories.withdraw_amount * 100) / total
    #print((percentage // 10) * 10 )

    print('Percentage spent by category')
    for i in range(100,-10,-10):
        print(f'{i:>3}|')
    print('-'*10)
    for i in categories.category:
        print(f'{i:>{line}}')

create_spend_chart(f)
