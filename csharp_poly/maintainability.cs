/* How does Polymorphism improve Code Maintainability and Extensibility? Provide a Scenario. 

Answer:
Polymorphism improves code maintainability and extensibility by allowing a single interface to represent different 
underlying data types. This means that code can be extended with new functionality without modifying existing code, 
reducing the risk of errors and making maintenance easier.
*/

using System;

// Base class
public abstract class Animal
{
    public abstract void Speak();
}

public class Dog : Animal
{
    public override void Speak()
    {
        Console.WriteLine("Woof!");
    }
}

public class Cat : Animal
{
    public override void Speak()
    {
        Console.WriteLine("Meow!");
    }
}

public class Program
{
    public static void Main()
    {
        Animal dog = new Dog();
        Animal cat = new Cat();

        dog.Speak();
        cat.Speak();
    }
}