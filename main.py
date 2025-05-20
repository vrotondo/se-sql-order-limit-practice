# Add to main.py

import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')
pd.read_sql("""
SELECT *
 FROM products;
""", conn)

# Ordering product code
ordering_product_code = pd.read_sql("""
SELECT *
 FROM products
ORDER BY productCode DESC;
""", conn)

# Product line and name
product_line_name = pd.read_sql("""
SELECT productCode, productLine, productName, productVendor
 FROM products
ORDER BY productLine, productName;
""", conn)

# Count
count = pd.read_sql("""
SELECT COUNT(DISTINCT productLine) AS productLineCount
 FROM products
""", conn)

# Query
query = pd.read_sql("""
SELECT productName, quantityInStock, MSRP, buyPrice, MSRP - buyPrice AS difference
 FROM products
ORDER BY difference DESC, CAST(quantityInStock AS INTEGER) ASC;
""", conn)

query2 = pd.read_sql("""
SELECT productName, productLine, MSRP, buyPrice, abs(buyPrice - MSRP) AS abs_difference
 FROM products
 WHERE productLine ="Classic Cars"
ORDER BY abs_difference DESC
LIMIT 10;
""", conn)

conn.close()