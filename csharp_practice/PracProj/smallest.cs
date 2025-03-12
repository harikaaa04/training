// Finding the smallest element in an array

using System;

class Program
{
    static void Main()
    {
        int[] numbers = { 5, 3, 9, 1, 6 };
        int smallest = FindSmallest(numbers);
        Console.WriteLine("The smallest elem ent is: " + smallest);
    }

    static int FindSmallest(int[] arr)
    {
        int min = arr[0];
        for (int i = 1; i < arr.Length; i++)
        {
            if (arr[i] < min)
            {
                min = arr[i];
            }
        }
        return min;
    }
}