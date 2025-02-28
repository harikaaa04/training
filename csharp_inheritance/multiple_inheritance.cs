/* Create two interfaces `IFlyable` and `ISwimmable` with methods `Fly()` and `Swim()`, respectively. 
Implement these interfaces in a class `Duck` to exhibit both behaviors. */

using System;

public interface IFlyable
{
    void Fly();
}

public interface ISwimmable
{
    void Swim();
}

public class Duck : IFlyable, ISwimmable
{
    public void Fly()
    {
        Console.WriteLine("I can fly.");
    }

    public void Swim()
    {
        Console.WriteLine("I can swim.");
    }
}

class Program
{
    static void Main()
    {
        Duck duck = new Duck();
        duck.Fly();
        duck.Swim();
    }
}