class bankaccount:

    def __init__(self,acount_holder,initial_balance):
        self.account_holder=acount_holder
        self.balance=initial_balance
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            return True
        return False
    
    def withdraw(self,amount):
        if(0<amount<=self.balance):
            self.balance-=amount
            return True
        return False
    
account=bankaccount("John",1000)

print("Account holder:",account.account_holder)

account.deposit(1500)
print("Balance after deposit:",account.get_balance())

account.withdraw(500)
print("Balance after withdraw:",account.get_balance())