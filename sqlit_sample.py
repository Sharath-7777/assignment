import sqlite3

db_connection = sqlite3.connect("strategy.db")
cursor = db_connection.cursor()
create_customer_query = "CREATE TABLE IF NOT EXISTS customer (customer_id INTEGER PRIMARY KEY, age INTEGER);"
cursor.execute(create_customer_query)
insert_customer_query = " INSERT INTO customer (customer_id, age) VALUES (100,19), (101, 20), (103, 23), (104, 40); "
cursor.execute(insert_customer_query)

create_sales_table = "CREATE TABLE IF NOT EXISTS sales (sales_id INTEGER PRIMARY KEY, customer_id INTEGER);"
cursor.execute(create_sales_table)

insert_sales_query = " INSERT INTO sales (sales_id, customer_id) VALUES (100,19), (101, 20), (103, 23), (104, 40); "
cursor.execute(insert_sales_query)