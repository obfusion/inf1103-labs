import os

def get_inventory_path(filename="inventory.txt"):
    if os.path.isabs(filename):
        return filename
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def load_inventory(filename="inventory.txt"):
    filepath = get_inventory_path(filename)
    orders = []
    transaction_history = []
    total_inventory = 0

    if os.path.exists(filepath):
        try:
            with open(filepath, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = [p.strip() for p in line.split(",")]
                    if len(parts) >= 3:
                        order_id = int(parts[0])
                        quantity = int(parts[-1])
                        product_name = ", ".join(parts[1:-1])
                        orders.append({
                            "id": order_id,
                            "product": product_name,
                            "quantity": quantity
                        })
                        transaction_history.append(quantity)
                        total_inventory += quantity
        except Exception as e:
            print(f"Error reading '{filename}': {e}")

    print("Current Orders:")
    if orders:
        for order in orders:
            print(f"{order['id']}, {order['product']}, {order['quantity']}")
        print("--------------------------")
    else:
        print("(No previous orders found)\n")

    return orders, total_inventory, transaction_history

def main():
    # Verify load_inventory parses existing records and establishes state
    orders, total_inventory, transaction_history = load_inventory()
    print(f"Loaded {len(orders)} orders. Starting total: {total_inventory}")

if __name__ == "__main__":
    main()