import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Devendra@24072000",  # Replace with your actual password
    database="retail_analytics"
)

# Read data from MySQL
query = "SELECT * FROM sales_data"
df = pd.read_sql(query, conn)

# Close connection
conn.close()

# Check data info
print(" Data Overview:")
print(df.info())
print("\n First 5 rows:")
print(df.head())

# Check for null values
print("\n Null Values:")
print(df.isnull().sum())

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\n Duplicate Rows: {duplicates}")

# Drop duplicates if any
if duplicates > 0:
    df = df.drop_duplicates()
    print(" Duplicates removed.")

# Save cleaned data to CSV (for R and Power BI)
cleaned_csv_path = "D:/CustomerSegmentationProject/data/cleaned_sales_data.csv"
df.to_csv(cleaned_csv_path, index=False)
print(f"\n Cleaned data saved to: {cleaned_csv_path}")
