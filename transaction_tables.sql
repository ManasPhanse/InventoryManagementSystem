use inventory;

CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    quantity INT,
    price FLOAT,
    warehouse_only BOOLEAN DEFAULT FALSE,
    product_id INT,
    location VARCHAR(100),
    FOREIGN KEY (product_id) REFERENCES products(id)
);


CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    store_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (store_id) REFERENCES stores(id)
);
