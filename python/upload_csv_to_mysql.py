import mysql.connector
import pandas as pd

# Load CSV
df = pd.read_csv("D:/CustomerSegmentationProject/data/sales_data.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devendra@24072000",  # Replace with your MySQL password
    database="retail_analytics"
)
cursor = conn.cursor()

# Insert rows
for _, row in df.iterrows():
    sql = """
    INSERT INTO sales_data (CustomerID, Gender, Age, AnnualIncome, SpendingScore, PurchaseAmount, PurchaseDate)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, tuple(row))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print(" Data inserted successfully!")

