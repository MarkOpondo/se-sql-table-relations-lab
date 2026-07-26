# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = """
SELECT firstName, lastName, jobTitle
FROM employees
JOIN offices
    USING(officeCode)
WHERE city = "Boston"
"""

# STEP 2
# Replace None with your code
df_zero_emp = """
SELECT *
FROM offices
JOIN employees 
    USING(officeCode)
GROUP BY officeCode
HAVING COUNT(employeeNumber) = 0
"""

# STEP 3
# Replace None with your code
df_employee = None

# STEP 4
# Replace None with your code
df_contacts = None

# STEP 5
# Replace None with your code
df_payment = None

# STEP 6
# Replace None with your code
df_credit = None

# STEP 7
# Replace None with your code
df_product_sold = None

# STEP 8
# Replace None with your code
df_total_customers = None

# STEP 9
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = None

# print(pd.read_sql("""SELECT * FROM offices""", conn))
print(pd.read_sql(df_zero_emp, conn))

conn.close()
