"""
Shopping Cart
- Create a program to simulate a shopping cart:
- Add items (item name and price).
- View cart items.
- Calculate the total price.
- Exit.
- Use functions and a loop to allow multiple actions.
"""

def add_item(cart, name, price):
    """Adds an item to the cart"""
    cart[name] = price 
    return cart

def view(cart):
    """View cart items"""
    print("Name, price")
    for name in cart:
        print(f"{name}: {cart[name]}")
    

def total(cart):
    """Calculates the total price"""
    tot = 0
    for price in cart.values():
        tot += price 
    return tot

def main():
    print("1. Add item\n2. View Cart\n3. Total Price\nEnter 'exit' to exit")
    cart = {}
    
    while True:
        opt = input("Please select an option: ")
        if opt == 'exit':
            return
        
        match int(opt):
            case 1:
                name = input("Name of the item: ")
                price = int(input("Price of the item: "))
                cart = add_item(cart, name, price)
                print(f"{name} has been added")
            case 2: 
                view(cart)
            case 3: 
                tot = total(cart)
                print(f"The total price is {tot}")
    
        
main()