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


def main():
    # Initial list storing product dictionaries
    inventory = [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    ]

    print("Initial Products:")
    display_all(inventory)

    print("\nAdding a product:")
    add_product(inventory)

    print("\nUpdated Inventory:")
    display_all(inventory)


if __name__ == "__main__":
    main()