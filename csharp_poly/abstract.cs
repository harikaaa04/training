/* Write a C# program demonstrating Polymorphism with an Abstract Class and Multiple Derived Classes. */

using System;

public abstract class Animal 
{
    public abstract void MakeSound();
    public void Sleep()
    {
        Console.WriteLine("Sleeping");
    }
}

public class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Woof");
    }
}

public class Cat : Animal
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
        Dog dog = new Dog();
        Cat cat = new Cat();

        dog.MakeSound();
        dog.Sleep();
        cat.MakeSound();
        cat.Sleep();
    }
}