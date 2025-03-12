/* What happens if a Base Class method is not marked as virtual but a Derived Class defines a method with the same name? 
Explain with an Example.

Answer:
If a base class method is not marked as virtual, but a derived class defines a method with the same name,
the derived method hides the base class method instead of overriding it. */

using System;

class Animal
{
    public void MakeSound() // Not marked as virtual
    {
        Console.WriteLine("Grr");
    }
}

class Dog : Animal
{
    public void MakeSound() // Hides the base method
    {
        Console.WriteLine("Woof Woof");
    }
}

class Program
{
    static void Main()
    {
        Animal animal = new Animal();
        animal.MakeSound(); 
        
        Animal aDog = new Dog();
        aDog.MakeSound(); 

        Dog dog = new Dog();
        dog.MakeSound(); 
    }
}



