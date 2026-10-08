import json
import os

FILENAME = "inventory.json"

def get_inventory_path(filename=FILENAME):
    if os.path.isabs(filename):
        return filename
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

### Checks whether inventory.json exists. Loads and returns its data if found; otherwise begins with an empty inventory
def load_inventory(filename=FILENAME):
    filepath = get_inventory_path(filename)
    if os.path.exists(filepath):
        print(f"{filename} found.")
        try:
            with open(filepath, "r") as file:
                inventory = json.load(file)
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading {filename}: {e}")
            return []
    else:
        print(f"{filename} not found. Beginning with an empty inventory.")
        return []

### Display all products in inventory
def display_all(inventory):
    print("Current Inventory")
    if not inventory:
        print("No products in inventory.")
        return
    for item in inventory:
        print(
            f"ID: {item['id']} | Name: {item['name']} | "
            f"Price: ${item['price']:.2f} | Stock: {item['stock']}"
        )

### Prompt user and append a new product dictionary to inventory
def add_product(inventory):
    print("\nAdd New Product")
    prod_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())
    except ValueError:
        print("Invalid input for price or stock quantity.")
        return

    new_product = {
        "id": prod_id,
        "name": name,
        "price": price,
        "stock": stock,
    }
    inventory.append(new_product)
    print("Product added successfully!")

### Search for product by ID and update its stock quantity
def update_stock(inventory):
    print("\nUpdate Stock")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"].lower() == prod_id.lower():
            print(f"\nProduct Found:\nName: {item['name']}\nCurrent Stock: {item['stock']}\n")
            try:
                new_stock = int(input("New Stock Quantity: ").strip())
                item["stock"] = new_stock
                print("\nStock updated successfully!")
            except ValueError:
                print("Invalid stock number entered.")
            return

    print("Product not found.")

### Search for a product by ID and display details if found
def search_product(inventory):
    print("\nSearch Product")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"].lower() == prod_id.lower():
            print("\nProduct Found")
            print("---------------------------------------------")
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Stock: {item['stock']}")
            print("---------------------------------------------")
            return

    print("\nProduct not found.")


def main():
    print("========================================\nINVENTORY MANAGEMENT SYSTEM\n========================================")
    inventory = load_inventory()

    menu_text = (
        "\n----------- MENU -----------\n"
        "1. Display All Products\n"
        "2. Add Product\n"
        "3. Update Stock\n"
        "4. Search Product\n"
        "5. Save Inventory\n"
        "6. Exit\n----------------------------"
    )
    print(menu_text)

    while True:
        choice = input("\nEnter option: ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("Save functionality not yet implemented in this phase.")
        elif choice == "6":
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()