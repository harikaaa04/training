/* Can we achieve Polymorphism with Structs in C#? Explain Why or Why Not. 

Answer:
No, we cannot achieve polymorphism with structs in C#.
Polymorphism in C# is typically achieved through inheritance and interfaces.
Structs in C# are value types and do not support inheritance.
*/

using System;

interface IShape
{
    void Draw();
}

struct Circle : IShape
{
    public void Draw()
    {
        Console.WriteLine("Drawing a Circle");
    }
}

struct Square : IShape
{
    public void Draw()
    {
        Console.WriteLine("Drawing a Square");
    }
}

class Program
{
    static void Main()
    {
        IShape shape1 = new Circle();
        IShape shape2 = new Square();

        shape1.Draw();
        shape2.Draw();
    }
}