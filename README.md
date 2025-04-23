# Practice for Ordering and Limiting Data with SQL


## Instructions

### Set Up
* Fork and Clone the Lab
* Install dependencies and open the virtual environment
    * `pipenv install`
    * `pipenv shell`
* Run main.py
    * `python3 main.py`

In `main.py`, import required libraries and connect to the database.

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')
pd.read_sql("""
SELECT *
  FROM products;
""", conn)
```

### Practice Queries

1. Begin by ordering the data by product code in descending order.

2. For this query:
* select the product code, product name, product line, and product vendor
* sort by product line and then product name

3. Now count how many distinct product lines there are.

4. For this query
* select the product name, quantity in stock, the MSRP, the buy price, and find the difference between the MSRP and buy price
 - Call this difference "difference"
* Order by the difference from the greatest to the least and then by quantiy in stock from least to greatest

5. For this query
* Select the product name, product line, the MSRP, the buy price
* find the difference between the buy price and MSRP, but use the absolute value to make the difference positive
 - Call this difference "abs_difference"
* Order by the difference from the greatest to the least
* Only select the "Classic Cars" product line
* limit the results to top 10