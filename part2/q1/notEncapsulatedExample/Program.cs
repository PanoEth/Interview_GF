using System;

public class MenuItem
{
    public string? Name;
    public float Price;

    public void ApplyDiscount(float discount)
        {
            if(discount < 0) //check if discount is negative [price - (-discount) = price + discount ]
            {
                Console.WriteLine("Discouint cannot be negative price.");
                return;
            }
                Price-= discount;
        }
}

class Program
{
    static void Main()
    {
        string Name = "Banana";
        var item1 = new MenuItem();
        item1.Name = Name;
        item1.Price = 1.50f;

        var item2 = new MenuItem();
        item2.Name = "ribeye steak";
        item2.Price = -15.00f;
        //Here we set price to MenuItem from main, since the property is public.

        Console.WriteLine($"First item is {item1.Name} and it costs {item1.Price}$.");
        Console.WriteLine($"Second item is {item2.Name} and it costs {item2.Price}$.");

        Console.Write($"Enter sale amount for {item1.Name}: ");
            float sale1 = float.Parse(Console.ReadLine());
        Console.Write($"Enter sale amount for {item2.Name}: ");
            float sale2 = float.Parse(Console.ReadLine());

        Console.WriteLine("\nAfter discount:");

        item1.ApplyDiscount(sale1);
        item2.ApplyDiscount(sale2);

        Console.WriteLine($"First item is {item1.Name} and it costs {item1.Price}$.");
        Console.WriteLine($"Second item is {item2.Name} and it costs {item2.Price}$.");
    }
}
