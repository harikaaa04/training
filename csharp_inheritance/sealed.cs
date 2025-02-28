/* Create a base class `Account` with a virtual method `CalculateInterest()`. 
Derive a class `SavingsAccount` and override `CalculateInterest()`. 
Now, prevent further overriding by marking it as `sealed`. */

using System;

public class Account
{
    public virtual void CalculateInterest()
    {
        Console.WriteLine("Calculating interest in Account class.");
    }
}

public class SavingsAccount : Account
{
    public sealed override void CalculateInterest()
    {
        Console.WriteLine("Calculating interest in SavingsAccount.");
    }
}

public class Program
{
    public static void Main()
    {
        Account acc = new Account();
        acc.CalculateInterest();

        SavingsAccount sAcc = new SavingsAccount();
        sAcc.CalculateInterest();
    }
}