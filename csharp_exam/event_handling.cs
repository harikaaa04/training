/* Create a `Button` class that has a delegate `OnClick`. 
Implement an event that triggers when the button is clicked. */
using System;

public class Button
{
    // Declare a delegate for the click event
    public delegate void ClickEventHandler(object sender, EventArgs e);

    // Declare the event using the delegate
    public event ClickEventHandler OnClick;

    // Method to simulate the button click
    public void Click()
    {
        // Check if there are any subscribers to the event
        if (OnClick != null)
        {
            // Trigger the event
            OnClick(this, EventArgs.Empty);
        }
    }
}

public class Program
{
    public static void Main()
    {
        // Create a new button instance
        Button button = new Button();

        // Subscribe to the OnClick event
        button.OnClick += Button_OnClick;

        // Simulate button click
        button.Click();
    }

    // Event handler method
    private static void Button_OnClick(object sender, EventArgs e)
    {
        Console.WriteLine("Button was clicked!");
    }
}
