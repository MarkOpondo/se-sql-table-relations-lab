# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

# pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""
SELECT firstName, lastName
FROM employees
JOIN offices
    USING(officeCode)
WHERE city = "Boston"
""", conn)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql("""
SELECT *
FROM offices
JOIN employees 
    USING(officeCode)
GROUP BY officeCode
HAVING COUNT(employeeNumber) = 0
""", conn)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
SELECT e.employeeNumber, e.firstName, e.lastName, o.city
FROM employees e
JOIN offices o 
    USING(officeCode)
ORDER BY e.firstName , e.lastName;
""", conn)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber
FROM customers c
WHERE NOT EXISTS(
    SELECT 1
    FROM orders o
    WHERE c.customerNumber = o.customerNumber                          
)
ORDER BY c.contactLastName ASC
""", conn)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
SELECT c.contactFirstName, c.contactLastName, p.paymentDate, p.amount
FROM customers c
JOIN payments p
    USING(customerNumber) 
ORDER BY p.amount DESC
""", conn)

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
print(df_payment)

conn.close()
