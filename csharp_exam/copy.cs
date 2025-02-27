/* Create a `Department` class with a reference-type property `Manager`. 
Implement both **Shallow Copy** and **Deep Copy** to show how references are handled.*/

using System;

public class Manager
{
    public string Name { get; set; }
}

public class Department : ICloneable
{
    public string DepartmentName { get; set; }
    public Manager Manager { get; set; }

    // Shallow copy
    public object Clone()
    {
        return this.MemberwiseClone();
    }

    // Deep copy
    public Department DeepCopy()
    {
        Department other = (Department)this.MemberwiseClone();
        other.Manager = new Manager { Name = this.Manager.Name };
        return other;
    }
}

class Program
{
    static void Main()
    {
        Department dept1 = new Department
        {
            DepartmentName = "HR",
            Manager = new Manager { Name = "John Doe" }
        };

        // Shallow copy
        Department dept2 = (Department)dept1.Clone();
        // Deep copy
        Department dept3 = dept1.DeepCopy();

        Console.WriteLine("Original Manager: " + dept1.Manager.Name);
        Console.WriteLine("Shallow Copy Manager: " + dept2.Manager.Name);
        Console.WriteLine("Deep Copy Manager: " + dept3.Manager.Name);

        // Change the manager's name in the original department
        dept1.Manager.Name = "Jane Smith";

        Console.WriteLine("\nAfter changing the original manager's name:");
        Console.WriteLine("Original Manager: " + dept1.Manager.Name);
        Console.WriteLine("Shallow Copy Manager: " + dept2.Manager.Name);
        Console.WriteLine("Deep Copy Manager: " + dept3.Manager.Name);
    }
}