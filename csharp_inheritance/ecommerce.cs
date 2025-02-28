/* Create a base class `Product` with properties `Name` and `Price`. 
Derive two classes `ElectronicProduct` and `ClothingProduct`. 
Add a `GetDiscountedPrice()` method in the base class and override it in the derived classes to apply different discount rules. */


using System;

public class Product
{
    public string Name {get; set;}
    public double Price {get; set;}

    public Product(string name, double price) 
    {
        Name = name;
        Price = price;
    }

    public virtual double GetDiscountedPrice()
    {
        return Price;
    }

    public virtual void DisplayInfo()
    {
        Console.WriteLine($"Product: {Name}, Original Price: {Price}, Discounted Price: {GetDiscountedPrice()}");
    }
}

public class ElectronicProduct : Product
{
    public ElectronicProduct(string name, double price) : base(name, price) {}

    public override double GetDiscountedPrice()
    {
        return Price * 0.9;
    }
}

public class ClothingProduct : Product
{
    public ClothingProduct(string name, double price) : base(name, price) {}
    public override double GetDiscountedPrice()
    {
        return Price * 0.8;
    }
}

class Program
{
    static void Main()
    {
        Product phone = new ElectronicProduct("iPhone", 100);
        Product shoes = new ClothingProduct("Nike", 100);

        phone.DisplayInfo();
        shoes.DisplayInfo();
    }
}