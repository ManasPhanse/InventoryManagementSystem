import mysql.connector
from getpass import getpass

# Connect to MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter Password: "),
        database="inventory"
    )

# Function to initialize the database with initial data
def insert_initial_data():
    conn = create_connection()
    cursor = conn.cursor()

    # Insert stores and warehouse
    cursor.execute("INSERT INTO stores (name) VALUES ('Store 1'), ('Store 2'), ('Store 3'), ('Store 4')")
    cursor.execute("INSERT INTO warehouses (name) VALUES ('Main Warehouse')")

    # Insert products
    cursor.execute("""
        INSERT INTO products (name, warehouse_only) VALUES
        ('Product A', TRUE),
        ('Product B', FALSE),
        ('Product C', TRUE),
        ('Product D', FALSE),
        ('Product E', FALSE)
    """)

    # Insert inventory for each product in warehouse and stores
    cursor.execute("""
        INSERT INTO inventory (product_id, product_name, location, quantity, price, warehouse_only) VALUES
        (1, 'Product A', 'Main Warehouse', 70, 10.0, TRUE),
        (1, 'Product A', 'Store 1', 10, 10.0, FALSE),
        (1, 'Product A', 'Store 2', 10, 10.0, FALSE),
        (1, 'Product A', 'Store 3', 5, 10.0, FALSE),
        (1, 'Product A', 'Store 4', 5, 10.0, FALSE),
        (2, 'Product B', 'Main Warehouse', 30, 15.0, FALSE),
        (2, 'Product B', 'Store 1', 10, 15.0, FALSE),
        (2, 'Product B', 'Store 2', 5, 15.0, FALSE),
        (2, 'Product B', 'Store 3', 3, 15.0, FALSE),
        (2, 'Product B', 'Store 4', 2, 15.0, FALSE),
        (3, 'Product C', 'Main Warehouse', 150, 20.0, TRUE),
        (3, 'Product C', 'Store 1', 20, 20.0, FALSE),
        (3, 'Product C', 'Store 2', 15, 20.0, FALSE),
        (3, 'Product C', 'Store 3', 10, 20.0, FALSE),
        (3, 'Product C', 'Store 4', 5, 20.0, FALSE),
        (4, 'Product D', 'Main Warehouse', 50, 25.0, FALSE),
        (4, 'Product D', 'Store 1', 10, 25.0, FALSE),
        (4, 'Product D', 'Store 2', 8, 25.0, FALSE),
        (4, 'Product D', 'Store 3', 4, 25.0, FALSE),
        (4, 'Product D', 'Store 4', 3, 25.0, FALSE),
        (5, 'Product E', 'Main Warehouse', 100, 30.0, FALSE),
        (5, 'Product E', 'Store 1', 25, 30.0, FALSE),
        (5, 'Product E', 'Store 2', 15, 30.0, FALSE),
        (5, 'Product E', 'Store 3', 5, 30.0, FALSE),
        (5, 'Product E', 'Store 4', 5, 30.0, FALSE)
    """)

    # Insert customers
    cursor.execute("""
        INSERT INTO customers (name, email, phone, address) VALUES
        ('John Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
        ('Jane Smith', 'jane.smith@example.com', '0987654321', '456 Elm St'),
        ('Alice Johnson', 'alice.johnson@example.com', '5556667777', '789 Oak St'),
        ('Bob Brown', 'bob.brown@example.com', '1112223333', '101 Pine St')
    """)

    conn.commit()
    cursor.close()
    print("Initial data inserted successfully!")

insert_initial_data()
