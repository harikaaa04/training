/* Create a base class `Person` and derive a class `Student`. 
Create an object of `Student`, upcast it to `Person`, and then downcast it back to `Student`. 
Demonstrate how type casting works. */

using System;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public void Display()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}");
    }
}

class Student : Person
{
    public int StudentID { get; set; }

    public void ShowStudentID()
    {
        Console.WriteLine($"Student ID: {StudentID}");
    }
}

class Program
{
    static void Main(string[] args)
    {
        Student student = new Student { Name = "Anu", Age = 20, StudentID = 12345 };

        // Upcast Student to Person
        Person person = student;

        // Downcast Person back to Student
        Student downcastedStudent = (Student)person;

        downcastedStudent.Display();
        downcastedStudent.ShowStudentID();
    }
}