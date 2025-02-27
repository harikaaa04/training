/*Define an interface `IPlayable` with a method `Play()`. 
Implement this interface in `MusicPlayer` and `VideoPlayer` classes with different implementations.*/

using System;

public interface IPlayable
{
    void Play();
}

public class MusicPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing music...");
    }
}

public class VideoPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing video...");
    }
}

class Program
{
    static void Main(string[] args)
    {
        IPlayable musicPlayer = new MusicPlayer();
        IPlayable videoPlayer = new VideoPlayer();

        musicPlayer.Play();
        videoPlayer.Play();
    }
}