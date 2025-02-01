"""
Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.
"""

class BankAccount:
    def __init__(self):
        self.balance = 0 
    
    def deposit(self, money):
        self.balance += money 
        print("The money has been deposited")
    
    def withdraw(self, money):
        if self.balance < money:
            print("Insufficient balance")
        else:
            self.balance -= money 
            print("The money has been withdrawn")

    
def main():
    bnk = BankAccount() 
    print("Enter 1 for deposit\nEnter 2 for withdraw\nEnter 3 to check for balance\nEnter 'exit' for exit")
    while True:
        opt = input("Enter option: ")
        if opt == "exit":
            return 
        
        match int(opt):
            case 1: 
                money = int(input("How much would you like to deposit? "))
                bnk.deposit(money)
            case 2: 
                money = int(input("How much would you like to withdraw? "))
                bnk.withdraw(money)
            case 3:
                print(f"The balance is {bnk.balance}")

main()        
        
        

    