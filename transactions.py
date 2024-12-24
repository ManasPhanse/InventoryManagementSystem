import mysql.connector
from getpass import getpass
from tabulate import tabulate

# Function to connect to MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter Password: "),
        database="inventory"
    )

# Function to display menu options
def display_menu():
    print("===== Inventory Management System =====")
    print("1. Add a product")
    print("2. Add product quantity")
    print("3. Delete a product")
    print("4. Modify a product")
    print("5. View inventory")
    print("6. Exit")

# Function to handle menu choices
def handle_choice(choice, conn):
    if choice == "1":
        add_product(conn)
    elif choice == "2":
        add_quantity(conn)
    elif choice == "3":
        delete_product(conn)
    elif choice == "4":
        modify_product(conn)
    elif choice == "5":
        view_inventory(conn)
    elif choice == "6":
        print("Exiting...")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

# Function to add a product
def add_product(conn):
    try:
        cursor = conn.cursor()
        name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        warehouse_only = input("Is this product warehouse-only? (yes/no): ").strip().lower() == 'yes'

        add_product_query = """
        INSERT INTO inventory (product_name, quantity, price, warehouse_only)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(add_product_query, (name, quantity, price, warehouse_only))
        conn.commit()
        print("Product added successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Function to add quantity to an existing product
def add_quantity(conn):
    try:
        cursor = conn.cursor()
        product_id = int(input("Enter the product ID: "))
        quantity = int(input("Enter the quantity to add: "))

        add_quantity_query = """
        UPDATE inventory
        SET quantity = quantity + %s
        WHERE id = %s
        """
        cursor.execute(add_quantity_query, (quantity, product_id))
        conn.commit()
        print("Quantity added to the product!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Function to delete a product
def delete_product(conn):
    try:
        cursor = conn.cursor()
        product_id = int(input("Enter the product ID to delete: "))

        delete_product_query = "DELETE FROM inventory WHERE id = %s"
        cursor.execute(delete_product_query, (product_id,))
        conn.commit()
        print("Product deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Function to modify a product
def modify_product(conn):
    try:
        cursor = conn.cursor()
        product_id = int(input("Enter the product ID to modify: "))

        # Check if the product exists
        check_product_query = "SELECT * FROM inventory WHERE id = %s"
        cursor.execute(check_product_query, (product_id,))
        product = cursor.fetchone()

        if product is None:
            print("Product not found!")
            return

        print("Current Product Details:")
        print("Product ID:", product[0])
        print("Product Name:", product[1])
        print("Quantity:", product[2])
        print("Price:", product[3])
        print("Warehouse Only:", "Yes" if product[4] else "No")

        name = input("Enter the new product name (leave blank to keep current): ")
        quantity = input("Enter the new quantity (leave blank to keep current): ")
        price = input("Enter the new price (leave blank to keep current): ")
        warehouse_only = input("Is this product warehouse-only? (yes/no, leave blank to keep current): ").strip().lower()
        if warehouse_only == 'yes':
            warehouse_only = True
        elif warehouse_only == 'no':
            warehouse_only = False
        else:
            warehouse_only = product[4]

        update_product_query = "UPDATE inventory SET product_name = %s, quantity = %s, price = %s, warehouse_only = %s WHERE id = %s"

        if name == "":
            name = product[1]
        if quantity == "":
            quantity = product[2]
        if price == "":
            price = product[3]

        cursor.execute(update_product_query, (name, quantity, price, warehouse_only, product_id))
        conn.commit()
        print("Product modified successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def view_inventory(conn):
    try:
        cursor = conn.cursor()
        print("===== Inventory =====")
        print("1. Sort by ID")
        print("2. Sort by Product Name")
        print("3. Sort by Quantity")
        print("4. Sort by Price")
        print("5. View Warehouse Only")
        print("6. Back to main menu")

        sort_choice = input("Enter your sort choice (1-6): ")

        if sort_choice == "1":
            sort_column = "id"
        elif sort_choice == "2":
            sort_column = "product_name"
        elif sort_choice == "3":
            sort_column = "quantity"
        elif sort_choice == "4":
            sort_column = "price"
        elif sort_choice == "5":
            sort_column = "warehouse_only"
        elif sort_choice == "6":
            return
        else:
            print("Invalid choice. Returning to main menu.")
            return

        view_inventory_query = f"SELECT id, product_name, quantity, price, warehouse_only FROM inventory ORDER BY {sort_column}"
        cursor.execute(view_inventory_query)
        inventory = cursor.fetchall()

        # Printing the inventory using tabulate
        print("======================================")
        if len(inventory) == 0:
            print("Inventory is empty!")
        else:
            headers = ["ID", "Product Name", "Quantity", "Price", "Warehouse Only"]
            formatted_inventory = [[product[0], product[1], product[2], product[3], "Yes" if product[4] else "No"] for product in inventory]
            print(tabulate(formatted_inventory, headers=headers, tablefmt="pretty"))
        print("======================================")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Main program loop
def main():
    conn = create_connection()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if not handle_choice(choice, conn):
            break
    
    conn.close()

if __name__ == "__main__":
    main()
