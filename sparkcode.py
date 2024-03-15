from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Create a SparkSession
spark = SparkSession.builder \
    .appName("SalesAnalysis") \
    .getOrCreate()

# Load data from your SQLite3 database into Spark DataFrames
# Assume you have already loaded the data into tables: sales, customer, orders, items
sales_df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlite:your_database_name.db") \
    .option("dbtable", "sales") \
    .load()

customer_df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlite:your_database_name.db") \
    .option("dbtable", "customer") \
    .load()

orders_df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlite:your_database_name.db") \
    .option("dbtable", "orders") \
    .load()

items_df = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlite:your_database_name.db") \
    .option("dbtable", "items") \
    .load()

# Join the DataFrames to get the required information
joined_df = sales_df.join(customer_df, sales_df["customer_id"] == customer_df["customer_id"]) \
    .join(orders_df, sales_df["order_id"] == orders_df["order_id"]) \
    .join(items_df, sales_df["item_id"] == items_df["item_id"])

# Filter customers aged 18-35 and sum quantities for each item
result_df = joined_df.filter((col("age") >= 18) & (col("age") <= 35)) \
    .groupBy("customer_id", "age", "item_name") \
    .agg(sum("quantity").alias("total_quantity"))

# Filter out items with no purchase (total quantity = 0)
result_df = result_df.filter(col("total_quantity") != 0)

# Convert DataFrame to Pandas DataFrame for writing to CSV
result_pandas_df = result_df.toPandas()

# Store the Pandas DataFrame to a CSV file with semicolon delimiter
result_pandas_df.to_csv("output.csv", sep=';', index=False)

# Stop the SparkSession
spark.stop()