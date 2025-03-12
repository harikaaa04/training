/* 
Explain how Interfaces and Abstract Classes enable Polymorphism. When should you use one over the other?

Answer:
Abstract Classes:
- Provide partial implementation (can have abstract & non-abstract methods).
- Use when classes share common behavior that should be inherited.

Interfaces:
- Define only method signatures (no implementation).
- Use when unrelated classes need to follow a common contract without inheritance. */

using System;

abstract class Animal
{
    public abstract void MakeSound();
    
    public void Sleep()
    {
        Console.WriteLine("Sleeping");
    }
}

class Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Bark");
    }
}

interface IVehicle
{
    void Drive();
}

class Car : IVehicle
{
    public void Drive()
    {
        Console.WriteLine("Driving a car");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Animal myDog = new Dog();
        myDog.MakeSound();
        myDog.Sleep();

        IVehicle myCar = new Car();
        myCar.Drive();
    }
}