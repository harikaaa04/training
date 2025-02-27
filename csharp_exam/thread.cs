/* Implement a Singleton class `ConfigurationManager` that prevents multiple instances. Ensure it is thread-safe. */

using System;

public sealed class ConfigurationManager
{
    // Step 1: Private static instance (lazy initialization)
    private static ConfigurationManager _instance;
    private static readonly object _lock = new object();

    // Step 2: Private constructor to prevent direct instantiation
    private ConfigurationManager()
    {
        Console.WriteLine("ConfigurationManager instance created.");
    }

    // Step 3: Public method to get the single instance (Thread-Safe)
    public static ConfigurationManager Instance
    {
        get
        {
            lock (_lock) // Ensures thread safety
            {
                if (_instance == null)
                {
                    _instance = new ConfigurationManager();
                }
                return _instance;
            }
        }
    }

    // Example method
    public void ShowMessage()
    {
        Console.WriteLine("Singleton ConfigurationManager is working.");
    }
}

// Example usage
public class Program
{
    static void Main()
    {
        ConfigurationManager config1 = ConfigurationManager.Instance;
        ConfigurationManager config2 = ConfigurationManager.Instance;

        config1.ShowMessage();

        // Verify that both variables refer to the same instance
        Console.WriteLine(ReferenceEquals(config1, config2)); // Output: True
    }
}
