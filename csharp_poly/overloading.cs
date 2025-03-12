/*  How does Method Overloading work in C#? Provide an Example where it is useful.

Answer:
Method Overloading allows multiple methods in the same class to have the same name but different parameters 
(different number, type, or order of parameters). It is a form of compile-time polymorphism. */

using System;

class Program
{
    // Method to add two integers
    public int Add(int a, int b)
    {
        return a + b;
    }

    // Overloaded method to add three integers
    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }

    // Overloaded method to add two doubles
    public double Add(double a, double b)
    {
        return a + b;
    }

    static void Main(string[] args)
    {
        Program program = new Program();

        Console.WriteLine("Add two integers: " + program.Add(1, 2));
        Console.WriteLine("Add three integers: " + program.Add(1, 2, 3));
        Console.WriteLine("Add two doubles: " + program.Add(1.5, 2.5));
    }
}