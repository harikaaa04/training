/* Create a `sealed` class `SecuritySystem` with a method `AuthenticateUser()`. 
Try to derive a class from it and observe the compiler error. 
Explain why `sealed` is useful in real-world applications. */


using System;

public sealed class SecuritySystem
{
    public void AuthenticateUser()
    {
        Console.WriteLine("Authenticating user");
    }
}

// public AdditionalSecurity : SecuritySystem
// {
//     public void ExtraSteps()
//     {
//         Console.WriteLine("Extra steps")
//     }
// }

class Program
{
    static void Main()
    {
        SecuritySystem sec = new SecuritySystem();
        sec.AuthenticateUser();
    }
}