import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
(1, 'Ali', 'Islamabad'),
(2, 'Sara', 'Lahore'),
(3, 'Bilal', 'Karachi'),
(4, 'Ayesha', 'Islamabad'),
(5, 'Hamza', 'Lahore'),
(6, 'Zain', 'Peshawar');

INSERT INTO orders VALUES
(1, 1, 8000),
(2, 1, 4500),
(3, 2, 7000),
(4, 2, 3000),
(5, 3, 9000),
(6, 3, 6000),
(7, 4, 5500),
(8, 4, 4000),
(9, 5, 6500),
(10, 6, 2500);
""")

conn.commit()
conn.close()

print("Database created successfully.")