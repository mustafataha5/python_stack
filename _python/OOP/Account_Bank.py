

class Account_Bank: 
    def __init__(self,balance=0,int_rate=0.01) :
        self.balance = balance 
        self.int_rate = int_rate
    
    def deposit(self, amount): 
        self.balance = self.balance+amount
        return self
    
    def withdraw(self, amount):
		# your code here
        if(self.balance - amount >= 0 ):
             self.balance = self.balance - amount 
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance  =self.balance - 5  
        return self       

    def display_account_info(self):
		# your code here
        print("Balance : ",self.balance)    
        return self
    
    def yield_interest(self):
		# your code here
        if(self.balance > 0):
            self.balance = self.balance + (self.balance*self.int_rate)       
        return self



account1 = Account_Bank(1000)
account2 = Account_Bank(1000,0.02)

account1.deposit(200).deposit(200).deposit(300).withdraw(1500).yield_interest().display_account_info()
account2.deposit(100).deposit(600).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()
    