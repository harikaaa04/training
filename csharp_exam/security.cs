/* Create a sealed class `SecuritySystem` that prevents inheritance. 
Show how sealing a class stops further extension */

public sealed class SecuritySystem
{
    public void Authenticate()
    {
        Console.WriteLine("Authentication successful.");
    }
}

// The following code will cause a compile-time error
// public class SecuritySystem2 : SecuritySystem
// {
// }