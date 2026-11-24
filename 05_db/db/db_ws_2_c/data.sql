-- Active: 1777358506531@@127.0.0.1@3306
SELECT
    "BillingCountry", sum(Total) AS TotalSales
FROM
    invoices
GROUP BY
    "BillingCountry";

SELECT
    strftime('%Y', InvoiceDate) AS Year, sum(Total) AS TotalSales
FROM
    invoices
GROUP BY
    Year;

SELECT
    "BillingCountry", max(Total) AS MaxOrderAmount
FROM
    invoices
WHERE
    "BillingCountry" = 'Germany'
    OR "BillingCountry" = 'France'
GROUP BY
    "BillingCountry";