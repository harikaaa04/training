class Customers:
    def __init__(self, name, orders):
        self.name = name
        self.orders = orders

class Orders():
    def __init__(self, order_id, description):
        self.order_id = order_id
        self.description = description

def main():
    name = input("Enter your name: ")
    
    orders = []
    print("Enter the orders (Enter 'exit' to exit): ")
    
    order_id = 1  
    while True:
        order_desc = input("Order: ")
        if order_desc.lower() == 'exit':
            break
        orders.append(Orders(order_id, order_desc))
        order_id += 1
    
    customer = Customers(name, orders)
    print(f"\nCustomer Name: {customer.name}")
    print("Orders:")
    for order in customer.orders:
        print(f"Order ID: {order.order_id}, Description: {order.description}")

if __name__ == "__main__":  
    main()
