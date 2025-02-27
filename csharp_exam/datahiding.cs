/* Create a `Student` class where `Name` and `RollNo` are private fields. 
Use properties to enforce validation (e.g., `RollNo` cannot be negative, `Name` cannot be empty).*/

using System;

class Student
{
    private string name;
    private int rollNo;

    public string Name
    {
        get { return name; }
        set
        {
            if (string.IsNullOrWhiteSpace(value))
            {
                throw new ArgumentException("Name cannot be empty.");
            }
            name = value;
        }
    }

    public int RollNo
    {
        get { return rollNo; }
        set
        {
            if (value < 0)
            {
                throw new ArgumentException("RollNo cannot be negative.");
            }
            rollNo = value;
        }
    }
}

class Program
{
    static void Main()
    {
        try
        {
            Student student = new Student();
            student.Name = "John Doe";
            student.RollNo = 123;

            Console.WriteLine($"Student Name: {student.Name}");
            Console.WriteLine($"Student RollNo: {student.RollNo}");
        }
        catch (ArgumentException ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
}