/* Modify the `DisplayInfo()` method in `Vehicle` to print `Brand` and `Speed`. 
Override this method in `Car` and `Bike` to include additional specific information. 
Ensure the base class method is called using `base.DisplayInfo()`. */

using System;

class Vehicle
{
    public string Brand { get; set; }
    public int Speed { get; set; }

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"Brand: {Brand}, Speed: {Speed}");
    }
}

class Car : Vehicle
{
    public int NumberOfDoors { get; set; }

    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"Number of Doors: {NumberOfDoors}");
    }
}

class Bike : Vehicle
{
    public bool freeHelmet { get; set; }

    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"Free Helmet: {freeHelmet}");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Car car = new Car { Brand = "Toyota", Speed = 120, NumberOfDoors = 4 };
        Bike bike = new Bike { Brand = "Yamaha", Speed = 80, freeHelmet = true };

        car.DisplayInfo();
        bike.DisplayInfo();
    }
}