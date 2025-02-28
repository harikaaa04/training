/* Create an interface `IMovable` with a method `Move()`. 
Implement this interface in a `Robot` class. 
Also, create a base class `Machine` with a method `Start()`. 
Have `Robot` inherit from `Machine` and implement `IMovable`. */

using System;

public interface IMovable
{
    void Move();
}

public class Machine 
{
    public void Start() 
    {
        Console.WriteLine("Starting...");
    }
}

public class Robot : Machine, IMovable
{
    public void Move() 
    {
        Console.WriteLine("I am a robot and I am moving.");
    }
}

class Program
{
    static void Main()
    {
        Robot robot = new Robot();
        robot.Start();
        robot.Move();
    }
}