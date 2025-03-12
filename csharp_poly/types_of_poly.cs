/* What is the difference between Compile-Time (Static) and Run-Time (Dynamic) Polymorphism in C#? Provide Code Examples. 

Answer:
Compile-Time Polymorphism (Static Polymorphism) occurs when method overloading or operator overloading is resolved at compile time, 
meaning the method to execute is determined before the program runs.

Run-Time Polymorphism (Dynamic Polymorphism) happens through method overriding, 
where the method to be executed is determined at runtime using virtual methods and inheritance.
*/


using System;

// Method overloading (compile time polymorphism)
class Addition
{
    public int Add(int a, int b) 
    {
        return a + b;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }
}

// Method overriding (run time polymorphism)
class Animal
{
    public virtual void MakeSound()
    {
        Console.WriteLine("Grr");
    }
}

class Cat : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Meow");
    }
}

class Program
{
    static void Main()
    {
        Addition sum = new Addition();
        Console.WriteLine(sum.Add(3, 8));
        Console.WriteLine(sum.Add(3.6, 4.8));

        Animal animal = new Animal();
        animal.MakeSound();
        Animal cat = new Cat();
        cat.MakeSound();
    }
}