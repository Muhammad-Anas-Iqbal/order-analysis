import sqlite3

conn = sqlite3.connect("orders.db")
cur = conn.cursor()

# (a) INNER JOIN
print("\n(a) Customer names and their order amounts:")

cur.execute("""
SELECT customers.name, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
""")

for row in cur.fetchall():
    print(row)


# (b) GROUP BY and SUM()
print("\n(b) Total amount spent by each customer:")

cur.execute("""
SELECT customers.name, SUM(orders.amount) AS total_spent
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id
ORDER BY total_spent DESC;
""")

for row in cur.fetchall():
    print(row)


conn.close()