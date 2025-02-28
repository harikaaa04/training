/* Create a class `Employee` with properties `Name` and `Salary`. 
Derive a class `Manager` that has an additional property `Bonus`. 
Use constructor chaining to initialize the properties from the base class. */

using System;

public class Employee
{
    public string Name {get; set;}
    public int Salary {get; set;}

    public Employee(string name, int salary)
    {
        Name = name;
        Salary = salary;
    }

    public virtual void DisplayInfo() 
    {
        Console.WriteLine($"Name: {Name}, Salary: {Salary}");
    }
}

public class Manager : Employee
{
    public int Bonus {get; set;}
    public Manager(string name, int salary, int bonus) : base(name, salary) 
    {
        Bonus = bonus;
    }

    public override void DisplayInfo()
    {
        base.DisplayInfo();
        Console.WriteLine($"Bonus: {Bonus}");
    }
}

class Program 
{
    static void Main()
    {
        Manager mgr = new Manager("Avani", 10000, 110);
        mgr.DisplayInfo();
    }
}