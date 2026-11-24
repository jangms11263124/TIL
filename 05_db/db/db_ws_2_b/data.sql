-- Active: 1777356583665@@127.0.0.1@3306
SELECT invoiceid, invoicedate FROM invoices;

SELECT 
    *
FROM 
    invoices;
WHERE
    billingcountry = 'USA'
    AND total > 10;

SELECT 
    *
FROM 
    invoices
WHERE
    BillingCity in ('London', 'Berlin');

SELECT 
    *
FROM 
    invoices
ORDER BY
    total DESC LIMIT 1;

SELECT 
    *
FROM 
    invoices
WHERE
    "InvoiceDate" > '2013-03-31'
    AND "Total" > 3;

SELECT 
    *
FROM 
    invoices
WHERE
    "BillingCountry" = 'USA'
    AND "BillingState" = 'CA'
    AND "Total" > 10;


SELECT 
    *
FROM 
    invoices
WHERE
    "BillingCountry" = 'Canada'
    AND "BillingState" = 'ON'
    AND "BillingCity" = 'Toronto';
SELECT 
    *
FROM 
    invoices
WHERE
    "InvoiceDate" < '2013-01-01'
    AND "BillingCountry" = 'Brazil'
    OR "Total" > 50;