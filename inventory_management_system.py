inventory = {}


def add_item():
    name = input("Enter item name: ").strip()
    if name in inventory:
        print("Item already exists.")
    else:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[name] = {"quantity": quantity, "price": price}
        print("Item added.")
def update_item():
    name = input("Enter item name to update: ").strip()
    if name in inventory:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        inventory[name] = {"quantity": quantity, "price": price}
        print("Item updated.")
    else:
        print("Item not found.")
def view_inventory():
    if not inventory:
        print("No items in inventory.")
    else:
        for name, details in inventory.items():
            print(f"{name} - Quantity: {details['quantity']}, Price: Rs{details['price']:.2f}")
def main():
    while True:
        print("\n1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Exit")
       
        choice = input("Choose an option (1-4): ").strip()


        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

