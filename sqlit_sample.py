
import sqlite3

db_connection = sqlite3.connect("strategy.db")
cursor = db_connection.cursor()
# Customer table
create_customer_query = "CREATE TABLE IF NOT EXISTS customer (customer_id INTEGER PRIMARY KEY, age INTEGER);"
cursor.execute(create_customer_query)
insert_customer_query = " INSERT INTO customer (customer_id, age) VALUES (100,19), (101, 20), (103, 33), (104, 40); "
cursor.execute(insert_customer_query)

# Sales Table
create_sales_table = "CREATE TABLE IF NOT EXISTS sales (sales_id INTEGER PRIMARY KEY, customer_id INTEGER);"
cursor.execute(create_sales_table)
insert_sales_query = """ INSERT INTO sales (sales_id, customer_id) VALUES (200,100), (201, 100), (203, 101), (204, 102),
                     (205, 103); """
cursor.execute(insert_sales_query)

# Orders Table
create_orders_table = """ CREATE TABLE IF NOT EXISTS orders (order_id INTEGER PRIMARY KEY, sales_id INTEGER,
                     item_id VARCHAR(255), quantity INTEGER);"""
cursor.execute(create_orders_table)
insert_orders_query = """ INSERT INTO orders (order_id, sales_id, item_id,quantity) VALUES (1000, 200, 'ITEM1', 10),
 (1001, 201, 'ITEM2', 1), (1002, 202, 'ITEM3', 1), (1003, 203, 'ITEM2', 1);"""
cursor.execute(insert_orders_query)

# Items Table
create_item_table = """ CREATE TABLE IF NOT EXISTS items (item_id VARCHAR(255) PRIMARY KEY, item_name VARCHAR(25));"""
cursor.execute(create_item_table)
insert_items_query = """INSERT INTO items (item_id, item_name) VALUES ('ITEM1', 'X'), ('ITEM2', 'Y'), ('ITEM3', 'Z') """
cursor.execute(insert_items_query)

db_connection.commit()
db_connection.close()