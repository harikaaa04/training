/*Create a base class `Vehicle` with a method `Start()`. 
Override it in `Car` and `Bike` classes to provide specific implementations. 
Use the `override` keyword and demonstrate polymorphism. */

using System;

class Vehicle
{
    public virtual void Start()
    {
        Console.WriteLine("Vehicle is starting");
    }
}

class Car : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Car is starting");
    }
}

class Bike : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Bike is starting");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Vehicle myCar = new Car();
        Vehicle myBike = new Bike();

        myCar.Start(); // Output: Car is starting
        myBike.Start(); // Output: Bike is starting
    }
}