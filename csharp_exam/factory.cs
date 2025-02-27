/* Implement a `VehicleFactory` class that returns different vehicle objects (`Car`, `Bike`) based on an input parameter. */

using System;

public interface IVehicle
{
    void Drive();
}

public class Car : IVehicle
{
    public void Drive()
    {
        Console.WriteLine("Driving a car.");
    }
}

public class Bike : IVehicle
{
    public void Drive()
    {
        Console.WriteLine("Riding a bike.");
    }
}

public class VehicleFactory
{
    public IVehicle GetVehicle(string vehicleType)
    {
        switch (vehicleType.ToLower())
        {
            case "car":
                return new Car();
            case "bike":
                return new Bike();
            default:
                throw new ArgumentException("Invalid vehicle type");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        VehicleFactory factory = new VehicleFactory();

        IVehicle vehicle1 = factory.GetVehicle("car");
        vehicle1.Drive();

        IVehicle vehicle2 = factory.GetVehicle("bike");
        vehicle2.Drive();
    }
}