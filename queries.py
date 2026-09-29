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

# (c) Cities where average order amount exceeds Rs. 5000
print("\n(c) Cities with average order amount greater than Rs. 5000:")

cur.execute("""
SELECT customers.city, AVG(orders.amount) AS average_order
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.city
HAVING AVG(orders.amount) > 5000;
""")

for row in cur.fetchall():
    print(row)

conn.close()