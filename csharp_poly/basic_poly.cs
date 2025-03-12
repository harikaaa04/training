/* Explain Polymorphism in C# with a Real-World Example.

Answer: 
Polymorphism allows methods to have different implementations based on the object calling them.
It can be method overloading or method overriding. */

using System;

class Animal
{
    public virtual void MakeSound()
    {
        Console.WriteLine("Grr");
    }
}

class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Woof Woof");
    }
}

class Cat : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Meow Meow");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Animal animal = new Animal();
        Animal dog = new Dog();
        Animal cat = new Cat();

        animal.MakeSound();
        dog.MakeSound();
        cat.MakeSound();
    }
}