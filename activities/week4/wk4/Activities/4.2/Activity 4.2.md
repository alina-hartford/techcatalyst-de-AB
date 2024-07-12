# SQL Activity 4.2

Make sure to create these tables in your schema in the `Techcatalyst_DE` database for example `techcatalyst_de.tatwan`

#### Step 1: Create Temporary Tables

**Schema:**

- **Table 1: Customers**
  - `customer_id` (INT, **Primary** Key)
  - `first_name` (VARCHAR)
  - `last_name` (VARCHAR)
  - `email` (VARCHAR)
- **Table 2: Orders**
  - `order_id` (INT, **Primary** Key)
  - `customer_id` (INT, **Foreign Key referencing Customers**)
  - `order_date` (DATE)
  - `total_amount` (DECIMAL)
- **Table 3: Products**
  - `product_id` (INT, **Primary** Key)
  - `product_name` (VARCHAR)
  - `price` (DECIMAL)



#### Step 2: Insert Data into Tables

You will need to insert 5 rows for each table. The following is an example. 

**Sample `INSERT` statements:**

```sql
-- Customers table
INSERT INTO Customers (customer_id, first_name, last_name, email)
VALUES (1, 'John', 'Doe', 'john.doe@example.com');

-- Orders table
INSERT INTO Orders (order_id, customer_id, order_date, total_amount)
VALUES (1, 1, '2023-01-01', 100.00);

-- Products table
INSERT INTO Products (product_id, product_name, price)
VALUES (1, 'Laptop', 999.99);

```



#### Step 3: Join the Tables

You will need to make sure that all three tables can be joined. You final query will be to show all columns from all three tables. 

**Write a query to join all three tables:**

* The `Orders` table has a foreign key `customer_id` that references the `customer_id` in the `Customers` table. This relationship implies that each order is associated with a specific customer.

* To create a meaningful join between the `Orders` and `Products` tables, we need an intermediary table to handle the many-to-many relationship, since one order can contain multiple products, and one product can be part of multiple orders. This intermediary table is typically called `OrderDetails`.

  

**Create the `OrderDetails` Table:**

**Schema:**

- OrderDetails
  - `order_id` (INT, **Foreign Key referencing Orders**)
  - `product_id` (INT, **Foreign Key referencing Products**)
  - `quantity` (INT)

Example insert

```sql
INSERT INTO OrderDetails (order_id, product_id, quantity)
VALUES (1, 1, 2);

```

