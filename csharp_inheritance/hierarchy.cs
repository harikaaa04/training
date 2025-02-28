/* Create a base class `Vehicle` with properties `Brand` and `Speed`. 
Derive two classes `Car` and `Bike` from `Vehicle`. 
Add a method `DisplayInfo()` in `Vehicle` that should be accessible in the derived classes. */

using System;

public class Vehicle
{
    public string Brand {get; set;}
    public int Speed {get; set;}

    public Vehicle(string brand, int speed) 
    {
        Brand = brand;
        Speed = speed;
    }

    public void DisplayInfo()
    {
        Console.WriteLine($"Brand: {Brand}, Speed: {Speed}");
    }
}

public class Car : Vehicle
{
    public Car(string brand, int speed) : base(brand, speed) {}
}

public class Bike : Vehicle
{
    public Bike(string brand, int speed) : base(brand, speed) {}
}

class Program
{
    static void Main() 
    {
        Car myCar = new Car("Toyota", 120);
        Bike myBike = new Bike("Yamaha", 80);

        myCar.DisplayInfo();
        myBike.DisplayInfo();
    }
}