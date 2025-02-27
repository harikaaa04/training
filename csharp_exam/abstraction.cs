/* Design an abstract class `Shape` with an abstract method `CalculateArea()`. 
Create derived classes `Circle` and `Rectangle` that implement this method. 
Demonstrate abstraction by instantiating these classes.	 */

using System;

abstract class Shape
{
    public abstract double CalculateArea();
}

class Circle : Shape
{
    private double radius;

    public Circle(double radius)
    {
        this.radius = radius;
    }

    public override double CalculateArea()
    {
        return Math.PI * radius * radius;
    }
}

class Rectangle : Shape
{
    private double width;
    private double height;

    public Rectangle(double width, double height)
    {
        this.width = width;
        this.height = height;
    }

    public override double CalculateArea()
    {
        return width * height;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Shape circle = new Circle(5);
        Console.WriteLine("Area of Circle: " + circle.CalculateArea());

        Shape rectangle = new Rectangle(4, 6);
        Console.WriteLine("Area of Rectangle: " + rectangle.CalculateArea());
    }
}