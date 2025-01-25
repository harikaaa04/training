"""
ATM Simulation
- Create a program to simulate an ATM where users can:
- Check balance
- Deposit money
- Withdraw money
- Exit
- Use functions for each operation and implement proper input validation (e.g., insufficient
balance for withdrawal).
"""

def deposit(balance, money):
    """Deposit money into the bank"""
    print("Money has been deposited")
    return balance + money

def withdraw(balance, money):
    """Withdraw money from the bank"""
    if money > balance:
        print("Insufficient balance for withdrawal")
        return balance
    print("Money has been withdrawn")
    return balance - money 

def main():
    balance = 0 
    print("1. Deposit money\n2. Withdraw money\n3. Check Balance\nEnter 'exit' to exit")
    while True:
        opt = input("Select an option: ")
        if opt == 'exit':
            return 
        match int(opt):
            case 1:
                money = int(input("How much money would you like to deposit? "))
                balance = deposit(balance, money)
            case 2: 
                money = int(input("How much money would you like to withdraw? "))
                balance = withdraw(balance, money)
            case 3:
                print(f"The bank balance is Rs. {balance}")


main()