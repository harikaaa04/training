/*Create a base class `User` with properties like `Username` and `Role`. 
Derive `Admin` and `Customer` classes that override a method `AccessControl()`, where `Admin` can access all features, 
but `Customer` has limited access.*/

using System;

public class User
{
    public string Username { get; set; }
    public string Role { get; set; }

    public virtual void AccessControl()
    {
        Console.WriteLine("Access control method in User class.");
    }
}

public class Admin : User
{
    public Admin()
    {
        Role = "Admin";
    }

    public override void AccessControl()
    {
        Console.WriteLine("Admin has access to all features.");
    }
}

public class Customer : User
{
    public Customer()
    {
        Role = "Customer";
    }

    public override void AccessControl()
    {
        Console.WriteLine("Customer has limited access.");
    }
}

class Program
{
    static void Main(string[] args)
    {
        User admin = new Admin { Username = "adminUser" };
        User customer = new Customer { Username = "customerUser" };

        admin.AccessControl();
        customer.AccessControl();
    }
}