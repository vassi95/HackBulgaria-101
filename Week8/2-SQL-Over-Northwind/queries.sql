--1
SELECT FirstName || " " || LastName AS full_name,
Title 
FROM employees;

--2
SELECT FirstName,
LastName
FROM employees
WHERE City = 'Seattle';

--3
SELECT FirstName,
LastName
FROM employees
WHERE City = 'London';

--4
SELECT FirstName,
LastName
FROM employees
WHERE Title LIKE  '%Sales%';

--5
SELECT FirstName,
LastName
FROM employees
WHERE TitleOfCourtesy  IN ('Ms.',  'Mrs.');

--6
SELECT FirstName,
LastName
FROM employees
ORDER BY BirthDate
LIMIT 5;

--7
SELECT FirstName,
LastName
FROM employees
ORDER BY HireDate
LIMIT 5;

--8
SELECT FirstName,
LastName
FROM employees
WHERE ReportsTo  IS NULL;

--9
SELECT e1.FirstName || " " ||
e1.LastName AS employee_name, e2.FirstName || " " ||
e2.LastName AS manager_name
FROM employees AS e1
LEFT JOIN employees AS e2
ON e1.ReportsTo = e2.EmployeeID;

--10
SELECT FirstName,
LastName
FROM employees
WHERE TitleOfCourtesy = 'Ms.'
OR TitleOfCourtesy = 'Mrs.';

--11
SELECT FirstName,
LastName
FROM employees
WHERE TitleOfCourtesy != 'Ms.'
AND TitleOfCourtesy != 'Mrs.';


--12
SELECT City,
COUNT(*) AS count_of_people
FROM employees
GROUP BY City;

--13
SELECT OrderID,
FirstName || " " || LastName
AS Employee_name
FROM orders 
JOIN employees
ON orders.EmployeeID=employees.EmployeeID;

--14
SELECT OrderID, CompanyName
FROM orders
JOIN shippers
ON orders.ShipVia=shippers.ShipperID;

--15
SELECT ShipCountry,
COUNT(*) FROM orders
GROUP BY ShipCountry;

--16
SELECT 
COUNT(*) AS c FROM orders o
GROUP BY EmployeeID
ORDER BY c DESC
LIMIT 1;

--17
SELECT CompanyName, COUNT(orders.CustomerID) AS Orders
FROM customers 
JOIN orders
ON customers.CustomerID==orders.CustomerID
GROUP BY customers.CustomerID
ORDER BY Orders DESC 
LIMIT 1;

--18
SELECT orders.OrderID,
 employees.FirstName || " " || employees.LastName
AS Employee_Name, 
customers.CompanyName 
FROM orders
JOIN employees ON employees.EmployeeID=orders.EmployeeID
JOIN customers ON customers.CustomerID=orders.CustomerID;

--19
SELECT customers.CompanyName, shippers.CompanyName
FROM customers
JOIN shippers ON customers.CustomerID 
IN (SELECT orders.CustomerID
FROM orders
WHERE orders.ShipVia = shippers.ShipperID);