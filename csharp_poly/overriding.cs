/* How does Method Overriding work in C#? Demonstrate with Code and Explain the `override`, `virtual`, and `new` Keywords.

Answer:
Method Overriding allows a derived class to provide a new implementation of a method defined in its base class.

virtual: Declares a method in the base class that can be overridden.
override: Overrides a virtual method in the derived class.
new: Hides the base class method instead of overriding it. */

using System;

public Animal
{
    public virtual void MakeSound()
    {
        Console.WriteLine("Grr");
    }
}

public Dog : Animal
{
    public override void MakeSound()
    {
        Console.WriteLine("Woof Woof");
    }
}

public Cat : Animal 
{
    public new void MakeSound()
    {
        Console.WriteLine("Meow Meow");
    }
}

class Program
{
    static void Main()
    {
        Animal animal = new Animal();
        animal.MakeSound();
        Animal dog = new Dog();
        dog.MakeSound();
        Animal cat = new Animal();
        cat.MakeSound();
    }
}