import threading
import time
import uuid

class Order:
    def __init__(self, menu_item, quantity):
        self.id = str(uuid.uuid4())[:8]
        self.menu_item = menu_item
        self.quantity = quantity
        self.status = "ordered"

def print_orders(orders):
    print("Orders:")
    for order in orders:
        print(f"ID: {order.id} | Menu Item: {order.menu_item.capitalize()} | Quantity: {order.quantity} | Status: {order.status}")

def print_menu(menu):
    print("Menu:")
    for item, details in menu.items():
        print(f"{item.capitalize()}: ₹{details['price']:.2f} (Stock: {details['stock']})")


def place_order(menu):
    orders = []
    while True:
        print_menu(menu)
        print("Enter 'done' to finish placing orders.")
        food_item = input("Enter the food item you want to order: ").strip().lower()
        if food_item == "done":
            break

        if food_item not in menu:
            print("Invalid food item. Please try again.")
            continue

        quantity = input("Enter the quantity: ")
        while not quantity.isdigit():
            print("Invalid input. Please enter a valid quantity.")
            quantity = input("Enter the quantity: ")

        quantity = int(quantity)
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        if quantity > menu[food_item]["stock"]:
            print("Sorry, we don't have enough stock for your order.")
            continue

        menu[food_item]["stock"] -= quantity
        order = Order(food_item, quantity)
        orders.append(order)

    return orders

def update_order_status(order):
    time.sleep(10)
    order.status = "preparing"
    time.sleep(10)
    order.status = "ready for pickup"
    time.sleep(10)
    order.status = "delivered"

def manage_orders(orders):
    while True:
        print("\n")
        print_orders(orders)
        print("Enter 'filter' to filter orders by status.")
        print("Enter 'exit' to return to the main menu.")
        
        command = input("Enter your choice: ").strip().lower()
        
        if command == "filter":
            status_filter = input("Enter the status to filter by (e.g., ordered, preparing, ready for pickup, delivered): ").strip().lower()
            filtered_orders = [order for order in orders if order.status == status_filter]
            print("\nFiltered Orders:")
            print_orders(filtered_orders)
        elif command == "exit":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid command. Please try again.")


def manage_inventory(menu):
    while True:
        print("\n")
        print_menu(menu)
        print("Enter 'add' to add new items to the inventory.")
        print("Enter 'update' to update the price of an existing item.")
        print("Enter 'restock' to restock an existing item.")
        print("Enter 'exit' to go back to the main menu.")

        command = input("Enter your choice: ").strip().lower()

        if command == "add":
            item_name = input("Enter the name of the new item: ").strip().lower()
            if item_name in menu:
                print("Item already exists in the inventory.")
                continue

            price = float(input("Enter the price of the item: "))
            stock = int(input("Enter the initial stock quantity: "))
            menu[item_name] = {"price": price, "stock": stock}
            print(f"{item_name.capitalize()} has been added to the inventory.")
        elif command == "update":
            item_name = input("Enter the name of the item to update: ").strip().lower()
            if item_name not in menu:
                print("Item not found in the inventory.")
                continue

            new_price = float(input("Enter the new price of the item: "))
            menu[item_name]["price"] = new_price
            print(f"{item_name.capitalize()} price has been updated.")
        elif command == "restock":
            item_name = input("Enter the name of the item to restock: ").strip().lower()
            if item_name not in menu:
                print("Item not found in the inventory.")
                continue

            quantity = int(input("Enter the quantity to restock: "))
            menu[item_name]["stock"] += quantity
            print(f"{item_name.capitalize()} has been restocked.")
        elif command == "exit":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid command. Please try again.")


def main():
    # Initialize the food menu with item, price (in rupees), and stock
    menu = {
        "burger": {"price": 450.00, "stock": 10},
        "pizza": {"price": 799.00, "stock": 15},
        "fries": {"price": 199.00, "stock": 20},
        "soda": {"price": 90.00, "stock": 30},
    }

    print("Welcome to the Food Canteen!")

    orders = []
    order_thread_pool = []

    while True:
        print("\n")
        print("Enter 'order' to place an order.")
        print("Enter 'inventory' to manage the inventory.")
        print("Enter 'manage orders' to manage the orders.")
        print("Enter 'exit' to quit the application.")

        command = input("Enter your choice: ").strip().lower()

        if command == "order":
            user_orders = place_order(menu)
            for order in user_orders:
                orders.append(order)
                order_thread = threading.Thread(target=update_order_status, args=(order,))
                order_thread.start()
                order_thread_pool.append(order_thread)
            print("Order(s) placed successfully!")
        elif command == "inventory":
            manage_inventory(menu)
        elif command == "manage orders":
            manage_orders(orders)
        elif command == "exit":
            print("Thank you for using the Food Canteen. Goodbye!")
            for thread in order_thread_pool:
                thread.join()  # Wait for all order threads to finish
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
