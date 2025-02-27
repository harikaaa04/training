/*Implement a `Book` class with three different constructors: 
(1) Default constructor, 
(2) Constructor with `Title` and `Author`, 
(3) Constructor with `Title`, `Author`, and `ISBN`. 
Ensure each constructor initializes properties correctly.*/

using System;

public class Book
{
    public string Title { get; set; }
    public string Author { get; set; }
    public string ISBN { get; set; }

    // Default constructor
    public Book()
    {
        Title = "Unknown";
        Author = "Unknown";
        ISBN = "000-0000000000";
    }

    // Constructor with Title and Author
    public Book(string title, string author)
    {
        Title = title;
        Author = author;
        ISBN = "000-0000000000";
    }

    // Constructor with Title, Author, and ISBN
    public Book(string title, string author, string isbn)
    {
        Title = title;
        Author = author;
        ISBN = isbn;
    }

    public void Display()
    {
        Console.WriteLine($"Title: {Title}, Author: {Author}, ISBN: {ISBN}");
    }
}

class Program
{
    static void Main()
    {
        Book book1 = new Book();
        Book book2 = new Book("1984", "George Orwell");
        Book book3 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565");

        book1.Display();
        book2.Display();
        book3.Display();
    }
}