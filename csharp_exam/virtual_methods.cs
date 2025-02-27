/*Create a `Person` base class with a `GetDetails()` method. 
Derive `Student` and `Teacher` classes that override `GetDetails()` to display their respective properties. 
Call `GetDetails()` using a base class reference. */

using System;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public virtual void GetDetails()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}");
    }
}

class Student : Person
{
    public string StudentID { get; set; }

    public override void GetDetails()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}, Student ID: {StudentID}");
    }
}

class Teacher : Person
{
    public string Subject { get; set; }

    public override void GetDetails()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}, Subject: {Subject}");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Person person1 = new Student { Name = "John", Age = 20, StudentID = "S12345" };
        Person person2 = new Teacher { Name = "Jane", Age = 35, Subject = "Math" };

        person1.GetDetails();
        person2.GetDetails();
    }
}