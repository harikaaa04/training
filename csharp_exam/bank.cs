/* Implement a `Bank` class with a static field `InterestRate` and a static method `SetInterestRate()`. 
Show how static members work across multiple objects. */

using System;

public class Bank
{
    public static double InterestRate { get; private set; }

    public static void SetInterestRate(double rate)
    {
        InterestRate = rate;
    }
}

public class Program
{
    public static void Main()
    {
        // Set interest rate using the static method
        Bank.SetInterestRate(4.5);
        Console.WriteLine("Interest Rate: " + Bank.InterestRate);

        // Create multiple Bank objects
        Bank bank1 = new Bank();
        Bank bank2 = new Bank();

        // Show that the static field is shared across all instances
        Console.WriteLine("Bank1 Interest Rate: " + Bank.InterestRate);
        Console.WriteLine("Bank2 Interest Rate: " + Bank.InterestRate);

        // Change the interest rate using one of the instances
        Bank.SetInterestRate(5.0);
        Console.WriteLine("Updated Interest Rate: " + Bank.InterestRate);
        Console.WriteLine("Bank1 Updated Interest Rate: " + Bank.InterestRate);
        Console.WriteLine("Bank2 Updated Interest Rate: " + Bank.InterestRate);
    }
}