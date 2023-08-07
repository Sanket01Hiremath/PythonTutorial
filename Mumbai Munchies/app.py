def print_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")


def place_order(menu):
    orders = {}
    while True:
        print_menu(menu)
        print("Enter 'done' to finish the order.")
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

        orders[food_item] = orders.get(food_item, 0) + quantity

    return orders


def calculate_total_bill(orders, menu):
    total_bill = 0
    for item, quantity in orders.items():
        total_bill += menu[item] * quantity
    return total_bill


def main():
    # Initialize the food menu with item and price
    menu = {
        "burger": 50,
        "pizza": 200,
        "fries": 50,
        "soda": 25,
    }

    print("Welcome To Mumbai Munchies")

    while True:
        print("\n")
        print("Enter 'order' to place an order.")
        print("Enter 'exit' to quit the application.")

        command = input("Enter your choice: ").strip().lower()

        if command == "order":
            user_orders = place_order(menu)
            total_bill = calculate_total_bill(user_orders, menu)
            print("\nOrder Summary:")
            for item, quantity in user_orders.items():
                print(f"{item.capitalize()}: {quantity} x ${menu[item]:.2f} = ${menu[item] * quantity:.2f}")

            print(f"Total Bill: ${total_bill:.2f}")
        elif command == "exit":
            print("Thank you for using the Mumbai Munchies. Come Again! Bye!")
            break
        else:
            print("Invalid command. Please try again.")



main()
