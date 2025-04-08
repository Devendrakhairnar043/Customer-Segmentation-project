-- Allow local file loading
SET GLOBAL local_infile = 1;

-- Use the database
USE retail_analytics;

-- Load data from CSV
LOAD DATA LOCAL INFILE 'D:/CustomerSegmentationProject/data/sales_data.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(CustomerID, Gender, Age, AnnualIncome, SpendingScore, PurchaseAmount, PurchaseDate);


SHOW VARIABLES LIKE 'local_infile';

SET GLOBAL local_infile = 1;

