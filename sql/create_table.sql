create database if not exists retail_analytics;
use retail_analytics;

CREATE TABLE IF NOT EXISTS sales_data (
    CustomerID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Age INT,
    AnnualIncome FLOAT,
    SpendingScore INT,
    PurchaseAmount FLOAT,
    PurchaseDate DATE
);
