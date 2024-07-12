# Removing Duplicates

Run the following in your schema

```sql
create or replace table fun_facts 
(
id INT PRIMARY KEY AUTOINCREMENT START 1 INCREMENT 1,
name string,
salary int,
other_id int unique 
);

insert into fun_facts
(name, salary, other_id)
values
('Tarek', 122.5, 123),
('Joe', 90.89, 123),
('Sara', 100, 123),
('Jack', 90.99, 150),
('Tarek', 122.5, 123),
('Joe', 90.89, 123),
('Sara', 100, 123),
('Jack', 90.99, 150);

select * from fun_facts;
```

Be ready to discuss the following in class:

* What is the `AUTOINCREMENT` doing?
* Why is Snowflake not enforcing constraints? 
* What are options you can use to remove or identify duplicates? 
  * Hint: they are familiar SQL statements you already have learned. How would you write your query?



