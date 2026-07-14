using System;

public class MenuItem
{
    public string? Name {get; set;}
    private float price;

    public float Price
    {
        get { return price; }
        set
        {
            if(value < 0.0f)
            {   //Checks if new price would be negative.
                Console.WriteLine($"Cannot set negative price for {Name}."); 
                return;
            }
            price = value;
        }
    }
        public MenuItem(string name, float initPrice)
        {
            Name = name;
            Price = initPrice;
        }

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
        var item1 = new MenuItem("Banana", 1.50f);
        var item2 = new MenuItem("Ribeye steak", 15.00f);
        Console.WriteLine($"{item1.Name} Costs: {item1.Price}$");
        Console.WriteLine($"{item2.Name} Costs: {item2.Price}$");
        
        Console.Write($"Enter sale amount for {item1.Name}: ");
            float sale1 = float.Parse(Console.ReadLine());
        Console.Write($"Enter sale amount for {item2.Name}: ");
            float sale2 = float.Parse(Console.ReadLine());

        Console.WriteLine("With discount: ");

        item1.ApplyDiscount(sale1);
        item2.ApplyDiscount(sale2); 

        Console.WriteLine($"{item1.Name} Costs: ${item1.Price}");
        Console.WriteLine($"{item2.Name} Costs: ${item2.Price}");
    }
}
