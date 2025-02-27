/* Define two interfaces `IPrintable` (for printing details) and `ISerializable` (for saving to a file). 
Implement both in a `Report` class and demonstrate multiple interface implementation*/

using System;
using System.IO;

interface IPrintable
{
    void Print();
}

interface ISerializable
{
    void Save(string filePath);
}

class Report : IPrintable, ISerializable
{
    public string Title { get; set; }
    public string Content { get; set; }

    public void Print()
    {
        Console.WriteLine("Title: " + Title);
        Console.WriteLine("Content: " + Content);
    }

    public void Save(string filePath)
    {
        using (StreamWriter writer = new StreamWriter(filePath))
        {
            writer.WriteLine("Title: " + Title);
            writer.WriteLine("Content: " + Content);
        }
    }
}

class Program
{
    static void Main()
    {
        Report report = new Report
        {
            Title = "Monthly Report",
            Content = "This is the content of the monthly report."
        };

        report.Print();

        string filePath = "report.txt";
        report.Save(filePath);
        Console.WriteLine("Report saved to " + filePath);
    }
}