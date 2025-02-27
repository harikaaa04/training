/* Implement an `INotificationObserver` interface where `EmailNotifier` and `SMSNotifier` listen for notifications. 
When a new message arrives, all observers should receive an update. */

using System;
using System.Collections.Generic;

public interface INotificationObserver
{
    void OnNotify(string message);
}

public class EmailNotifier : INotificationObserver
{
    public void OnNotify(string message)
    {
        Console.WriteLine("Email Notification: " + message);
    }
}

public class SMSNotifier : INotificationObserver
{
    public void OnNotify(string message)
    {
        Console.WriteLine("SMS Notification: " + message);
    }
}

public class NotificationService
{
    private List<INotificationObserver> observers = new List<INotificationObserver>();

    public void AddObserver(INotificationObserver observer)
    {
        observers.Add(observer);
    }

    public void RemoveObserver(INotificationObserver observer)
    {
        observers.Remove(observer);
    }

    public void NotifyObservers(string message)
    {
        foreach (var observer in observers)
        {
            observer.OnNotify(message);
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        NotificationService notificationService = new NotificationService();

        EmailNotifier emailNotifier = new EmailNotifier();
        SMSNotifier smsNotifier = new SMSNotifier();

        notificationService.AddObserver(emailNotifier);
        notificationService.AddObserver(smsNotifier);

        notificationService.NotifyObservers("New message received!");

        notificationService.RemoveObserver(emailNotifier);

        notificationService.NotifyObservers("Another message received!");
    }
}