/* Create an abstract class `Animal` with an abstract method `MakeSound()`. 
Derive two classes `Dog` and `Cat` that override `MakeSound()`. 
Instantiate objects of both classes and call the method. */

using System;

public abstract class Animal
{
    public abstract void MakeSound();
}

public class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Woof woof");
    }
}

public class Cat : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Meow meow");
    }
}

class Program
{
    static void Main()
    {
        Animal dog = new Dog();
        Animal cat = new Cat();

        dog.MakeSound();
        cat.MakeSound();
    }
}