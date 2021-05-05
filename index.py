class BankAccount:
    bank_name= "Bank of Sam"
    def __init__(self, account_name, int_rate, cash):
        self.account_name= account_name
        self.int_rate = int_rate
        self.cash= cash
    def deposit(self, dep):
        self.cash += dep
        return self
    def withdraw(self, wdraw):
        self.cash -= wdraw
        return self
    def display_account(self):
        self.display_account= print(f"{self.bank_name}, Account: {self.account_name}, Balance of: {self.cash}")
        return self
    def add_interest(self):
        if self.cash >0:
            self.cash = self.cash + (self.int_rate * self.cash)
        else:
            print("YOU ARE BROKE")
        return self


checking1= BankAccount("checking1", .10, 1000)
savings1= BankAccount("savings1", .20, 2000)
checking1.deposit(2000).deposit(2000).deposit(2000).withdraw(1000).add_interest().display_account()
savings1.deposit(10000).deposit(10000).withdraw(100).withdraw(100).withdraw(100).withdraw(150).add_interest().display_account()
