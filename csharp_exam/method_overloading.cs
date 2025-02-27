/*Implement a `Calculator` class with overloaded methods `Add()`. 
It should accept two integers, three integers, and two double values separately. 
Demonstrate how method overloading works.*/

using System;

class Calculator
{
    // Method to add two integers
    public int Add(int a, int b)
    {
        return a + b;
    }

    // Method to add three integers
    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }

    // Method to add two double values
    public double Add(double a, double b)
    {
        return a + b;
    }
}

class Program
{
    static void Main()
    {
        Calculator calc = new Calculator();

        // Demonstrate method overloading
        Console.WriteLine("Add two integers: " + calc.Add(1, 2));
        Console.WriteLine("Add three integers: " + calc.Add(1, 2, 3));
        Console.WriteLine("Add two doubles: " + calc.Add(1.1, 2.2));
    }
}