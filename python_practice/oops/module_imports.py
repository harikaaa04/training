from sales import Customers, Orders

def main():
    ord1 = Orders(1, "Shoes")
    ord2 = Orders(2, "Laptop")
    ord3 = Orders(3, "Chocolate")

    orders = [ord1, ord2, ord3]
    cust1 = Customers("Harika", orders)
    
    for ord in cust1.orders:
        print(f"Order ID: {ord.order_id}, Description: {ord.description}")


main()