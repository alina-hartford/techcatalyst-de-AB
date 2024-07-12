# Date and Time Functions

```sql
SELECT CURRENT_DATE() as TODAY_DATE, -- get today's date
                YEAR(TODAY_DATE) as year, -- extract year from date
                MONTH(TODAY_DATE) as month, -- extract month from date
                QUARTER(TODAY_DATE)as quarter, -- extract quarter from date
                WEEK(TODAY_DATE) as week, -- extract week number from date
                DAYNAME(TODAY_DATE) as name_of_day,  -- get name of day
                NEXT_DAY(TODAY_DATE,'WE') as next_date, -- get next date of a day 'mo', 'tu' ,'we', 'thu', 'fri', 'sa', 'su'
                PREVIOUS_DAY(TODAY_DATE ,'WE') as prev_date, -- get previous date of a day 'mo', 'tu' ,'we', 'thu', 'fri', 'sa', 'su'
                DATEADD('month', 1, TODAY_DATE) as next_month, -- add 'year', 'month', 'day', 'quarter' to a date
                DATEADD('quarter', 1, TODAY_DATE) as next_quarter,-- add 'year', 'month', 'day', 'quarter' to a date,
                DATEDIFF('day', TODAY_DATE, next_date) as diff_in_days, --get difference between two dates in days
                DATEDIFF('month', TODAY_DATE, next_quarter) as diff_in_months -- get difference between two dates in months
                ;
```



# Conversion Functions

**EXAMPLE: STRING TO DECIMAL**

```sql
SELECT
    CAST('124' as DECIMAL(5,2)), -- convert from string to decimal using CAST function
    '124'::DECIMAL(5,2), -- convert from string to decimal using ::
    TO_DECIMAL('123', 5,2), --convert from string to decimal using TO_DECIMAL function
    TRY_TO_DECIMAL('12A', 5,2) --convert from string to decimal using TO_DECIMAL function
    ;
```

**EXAMPLE: STRING TO DATE or DATETIME**

```sql
SELECT
    CAST('2023-10-25' as DATE), -- Convert String to Date using CAST function
    '2023-10-25'::DATE, -- Convert String to Date using ::
    CAST('2023-10-25' as DATETIME), -- Convert String to TimeStamp/DateTime using CAST
    '2023-10-25'::DATETIME, -- Convert String to TimeStamp/DateTime using ::
    TO_DATE('2023-10-25'), -- Convert String to Date using TO_DATE function
    TO_TIMESTAMP('2023-10-25') -- Convert String to TimeStamp/DateTime using TO_TIMESTAMP
    ;
    
SELECT
    TRY_CAST('202A-10-25' as DATE), -- Convert String to Date using CAST function
    '2023-10-25'::DATE, -- Convert String to Date using ::
    TRY_CAST('2023-10-25' as DATETIME), -- Convert String to TimeStamp/DateTime using CAST
    '2023-10-25'::DATETIME, -- Convert String to TimeStamp/DateTime using ::
    TRY_TO_DATE('202A-10-25'), -- Convert String to Date using TO_DATE function
    TRY_TO_TIMESTAMP('2023-10-25') -- Convert String to TimeStamp/DateTime using TO_TIMESTAMP
    ;
```



# Conditional Functions

**IFF**

```sql
SELECT
   IFF(1+1 = 2, 'Correct', 'Wrong') as logic_1,
   IFF(1+1 = 2, 1+1, 0) as logic_2,
   IFF(100 > 5, True, False),
   IFF('50'::int = 50, 'Integer', 'Non Integer'),
   IFF('0050'::int = 50, 'Integer', 'Non Integer'),
   is_integer(5.2),
   is_decimal(5.2);
```

