class Account_Bank: 
    def __init__(self,balance=0,int_rate=0.01,serial="") :
        self.balance = balance 
        self.int_rate = int_rate
        self.serial = serial

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



class User: 
    def __init__(self,name,balance=0) -> None:
        self.name = name 
        self.num_of_account = 1
        self.account = [Account_Bank(balance,serial="account-"+str(self.num_of_account))]

    def  make_deposit(self,num, amount):
        self.account[num].deposit(amount) 
        return self 
    
    def make_withdrawal(self,num,amount):
        self.account[num].withdraw(amount)
        return self       

    def display_user_balance(self,num):
        print("User name: ",self.name,f"{self.account[num].serial}   Balance: ",self.account[num].balance)
        return self

    def display_all_account(self):
        for i in self.account:
                    print("User name: ",self.name,f"{i.serial}   Balance: ",i.balance)
    def transfer_money(self, num,other,other_num, amount):
        self.make_withdrawal(num,amount)
        other.make_deposit(other_num,amount)
        return self
    
    def Create_Account(self,balance = 0): 
        # newAccount = Account_Bank(balance)
        # current = self.account 
        # while(current.next): 
        #     current = current.next
        # current = newAccount
        self.num_of_account = self.num_of_account+1
        self.account.append(Account_Bank(balance,serial="account-"+str(self.num_of_account)))
        
        return self



user1 = User("user1",1000)        
user2 = User("user2")
user3 = User("user3",200)


user1.display_user_balance(0).make_deposit(0,200).make_deposit(0,300).make_deposit(0,50).make_withdrawal(0,1000).display_user_balance(0)

user2.display_user_balance(0).make_deposit(0,200).make_deposit(0,1300).make_withdrawal(0,1000).display_user_balance(0)
user3.display_user_balance(0)
user3.make_deposit(0,500).make_withdrawal(0,100).make_withdrawal(0,400).make_withdrawal(0,1000).display_user_balance(0)
print("Make account-1 to user3 with 2000")
user3.Create_Account(2000)
user3.display_user_balance(1)
print("user1 transfer 100 to user3")

user1.transfer_money(0,user3,1,100)
user1.display_user_balance(0)
user3.display_all_account()















