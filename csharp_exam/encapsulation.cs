/* Create a `BankAccount` class where `balance` is a private field. 
Implement methods for `Deposit()` and `Withdraw()`, ensuring that withdrawal is only allowed if there is a sufficient balance. 
Prevent direct modification of `balance` from outside the class.*/

using System;

public class BankAccount
{
    private decimal balance;

    public BankAccount(decimal initialBalance)
    {
        balance = initialBalance;
    }

    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            balance += amount;
            Console.WriteLine($"Deposited: {amount:C}. New balance: {balance:C}");
        }
        else
        {
            Console.WriteLine("Deposit amount must be positive.");
        }
    }

    public void Withdraw(decimal amount)
    {
        if (amount > 0)
        {
            if (balance >= amount)
            {
                balance -= amount;
                Console.WriteLine($"Withdrew: {amount:C}. New balance: {balance:C}");
            }
            else
            {
                Console.WriteLine("Insufficient balance.");
            }
        }
        else
        {
            Console.WriteLine("Withdrawal amount must be positive.");
        }
    }

    public decimal GetBalance()
    {
        return balance;
    }
}

class Program
{
    static void Main()
    {
        BankAccount account = new BankAccount(1000);
        account.Deposit(500);
        account.Withdraw(200);
        account.Withdraw(1500);
        Console.WriteLine($"Final balance: {account.GetBalance():C}");
    }
}