/* Implement an `ILogger` interface and `FileLogger` class. 
Use the **Decorator Pattern** to add extra logging features like timestamp and error categorization. */

using System;
using System.IO;

public interface ILogger
{
    void Log(string message);
}

public class FileLogger : ILogger
{
    private readonly string _filePath;

    public FileLogger(string filePath)
    {
        _filePath = filePath;
    }

    public void Log(string message)
    {
        File.AppendAllText(_filePath, message + Environment.NewLine);
    }
}

public abstract class LoggerDecorator : ILogger
{
    protected readonly ILogger _logger;

    protected LoggerDecorator(ILogger logger)
    {
        _logger = logger;
    }

    public abstract void Log(string message);
}

public class TimestampLogger : LoggerDecorator
{
    public TimestampLogger(ILogger logger) : base(logger) { }

    public override void Log(string message)
    {
        string timestampedMessage = $"{DateTime.Now}: {message}";
        _logger.Log(timestampedMessage);
    }
}

public class ErrorCategorizationLogger : LoggerDecorator
{
    public ErrorCategorizationLogger(ILogger logger) : base(logger) { }

    public override void Log(string message)
    {
        string categorizedMessage = $"[ERROR]: {message}";
        _logger.Log(categorizedMessage);
    }
}

// Example usage
class Program
{
    static void Main()
    {
        ILogger logger = new FileLogger("log.txt");
        logger = new TimestampLogger(logger);
        logger = new ErrorCategorizationLogger(logger);

        logger.Log("This is a test error message.");
    }
}