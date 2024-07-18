# Spark ETL Project

## Introduction

### Project Description
* Sparkify, a music streaming startup, wants to move their processes and data onto the cloud. Their song data and user activity is stored in S3 as JSON files. 
* Build an ETL pipeline that extracts data from S3, stages them in a Data Lake, and transforms data into a set of dimensional tables in Snowflake
### ETL Process
* I first extracted all the song data JSON files from S3 and loaded them into Databricks so that I could utilize PySpark to transform the data into separate tables. I did the same process for all the user log data as well.
* I created 4 dimensional tables: Songs, Artists, Users and Time
   * For the Songs table I extracted the song_id, title, artist_id, year, and duration from the song data file. I partitioned this table by year and artist_id when I loaded the data back into S3 as a Parquet file.
   * For the Artists table I extracted distinct values of artist_id, artist_name, artist_location, artist_latitude, and artist_longitude. I did not apply any partitions and loaded this file as a Parquet back into S3.
### Data Lake and Data Warehouse

## Architecural Diagram
![Architectural_Diagram](https://github.com/user-attachments/assets/645bd199-9b25-4829-ba5c-15c2e3776093)

## Data in Amazon S3
User Log Data (Raw) : `s3://techcatalyst-public/log_data`

Song Data (Raw) : `s3://techcatalyst-public/song_data`

Transformed Data: `s3://techcatalyst-public/dw_stage/alina/`

![Transformed Data in S3](https://github.com/user-attachments/assets/e7abfb9d-87ba-43a6-9a97-44a19bcb91d9)

## Creating Tables in Snowflake
```sql
--creating SONGS_DIM table
CREATE OR REPLACE TRANSIENT TABLE TECHCATALYST_DE.ABABY.SONGS_DIM (
    SONG_ID STRING,
    SONG_TITLE STRING,
    ARTIST_ID STRING,
    SONG_YEAR NUMBER,
    SONG_DURATION FLOAT
);

--creating USER_DIM table
CREATE OR REPLACE TRANSIENT TABLE TECHCATALYST_DE.ABABY.USER_DIM (
    ID VARCHAR,
    FIRSTNAME VARCHAR,
    LASTNAME VARCHAR,
    GENDER VARCHAR,
    LEVEL VARCHAR
);

--creating TIME_DIM table
CREATE OR REPLACE TRANSIENT TABLE TECHCATALYST_DE.ABABY.TIME_DIM (
    TIME_ID STRING,
    DATETIME DATETIME,
    START_TIME TIME,
    YEAR NUMBER,
    MONTH NUMBER,
    DAYOFMONTH NUMBER,
    WEEKOFYEAR NUMBER
);

--creating ARTIST_DIM table
CREATE OR REPLACE TRANSIENT TABLE TECHCATALYST_DE.ABABY.ARTIST_DIM (
    ARTIST_ID VARCHAR,
    ARTIST_NAME VARCHAR,
    ARTIST_LOCATION VARCHAR,
    ARTIST_LATITUDE FLOAT,
    ARTIST_LONGITUDE FLOAT
);

--creating SONGPLAYS_FACT table
CREATE OR REPLACE TRANSIENT TABLE TECHCATALYST_DE.ABABY.SONGPLAYS_FACT (
    SONGPLAY_ID STRING,
    DATETIME_ID STRING,
    YEAR NUMBER,
    MONTH NUMBER,
    USER_ID STRING,
    LEVEL STRING,
    SONG_ID STRING,
    ARTIST_ID STRING,
    SESSION_ID STRING,
    LOCATION STRING,
    USER_AGENT STRING
);
```

## Inserting data into created tables in Snowflake
Before I inserted data into my tables, I made sure I set up my external stage so that I could access the data in my S3 Bucket. I also created a Parquet file format so that Snowflake would be able to read the Parquet files I had created. I then read and inspected the schema of the parquet files to understand which columns are accessible and what their types are.
```sql
--inserting data into SONGS_DIM table from songs_table in S3
INSERT INTO SONGS_DIM (SONG_ID, SONG_TITLE, ARTIST_ID, SONG_YEAR, SONG_DURATION)
SELECT
$1:song_id::STRING AS SONG_ID,
$1:title::STRING AS SONG_TITLE,
REGEXP_SUBSTR(METADATA$FILENAME, 'artist_id=([^/]+)', 1, 1, 'e')::STRING AS ARTIST_ID,
REGEXP_SUBSTR(METADATA$FILENAME, 'year=(\\d+)', 1, 1, 'e')::NUMBER AS SONG_YEAR,
$1:duration::FLOAT AS SONG_DURATION
FROM @TECHCATALYST_DE.EXTERNAL_STAGE.AB_STAGE/songs_table/ (FILE_FORMAT => 'TECHCATALYST_DE.EXTERNAL_STAGE.AB_PARQUET_FORMAT', PATTERN => '.*parquet.*');

--copying data into USER_DIM table from user_table in S3
COPY INTO TECHCATALYST_DE.ABABY.USER_DIM
FROM @TECHCATALYST_DE.EXTERNAL_STAGE.AB_STAGE/user_table/
PATTERN = '.*parquet.*'
FILE_FORMAT = 'TECHCATALYST_DE.EXTERNAL_STAGE.AB_PARQUET_FORMAT'
ON_ERROR = CONTINUE
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

--inserting data into TIME_DIM table from time_table in S3
INSERT INTO TIME_DIM (TIME_ID, DATETIME, START_TIME, YEAR, MONTH, DAYOFMONTH, WEEKOFYEAR)
SELECT
$1:ts::STRING AS TIME_ID,
$1:datetime::DATETIME AS DATETIME,
$1:start_time::TIME AS START_TIME,
REGEXP_SUBSTR(METADATA$FILENAME, 'year=(\\d+)', 1, 1, 'e')::NUMBER AS YEAR,
REGEXP_SUBSTR(METADATA$FILENAME, 'month=([^/]+)', 1, 1, 'e')::STRING AS MONTH,
$1:dayofmonth::NUMBER AS DAYOFMONTH,
$1:weekofyear::NUMBER AS WEEKOFYEAR
FROM @TECHCATALYST_DE.EXTERNAL_STAGE.AB_STAGE/time_table/ (FILE_FORMAT => 'TECHCATALYST_DE.EXTERNAL_STAGE.AB_PARQUET_FORMAT', PATTERN => '.*parquet.*');

--copying data into ARTIST_DIM table from artist_table in S3
COPY INTO TECHCATALYST_DE.ABABY.ARTIST_DIM
FROM @TECHCATALYST_DE.EXTERNAL_STAGE.AB_STAGE/artists_table/
PATTERN = '.*parquet.*'
FILE_FORMAT = 'TECHCATALYST_DE.EXTERNAL_STAGE.AB_PARQUET_FORMAT'
ON_ERROR = CONTINUE
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;

--inserting data into SONGPLAYS_FACT table from songsplay_table in S3
INSERT INTO SONGPLAYS_FACT (SONGPLAY_ID, DATETIME_ID, YEAR, MONTH, USER_ID, LEVEL, SONG_ID, ARTIST_ID, SESSION_ID, LOCATION, USER_AGENT)
SELECT
$1:songplay_id::STRING AS SONGPLAY_ID,
$1:datetime_id::STRING AS DATETIME_ID,
REGEXP_SUBSTR(METADATA$FILENAME, 'year=(\\d+)', 1, 1, 'e')::NUMBER AS YEAR,
REGEXP_SUBSTR(METADATA$FILENAME, 'month=([^/]+)', 1, 1, 'e')::STRING AS MONTH,
$1:user_id::STRING AS USER_ID,
$1:level::STRING AS LEVEL,
$1:song_id::STRING AS SONG_ID,
$1:artist_id::STRING AS ARTIST_ID,
$1:session_id::STRING AS SESSION_ID,
$1:location::STRING AS LOCATION,
$1:user_agent::STRING AS USER_AGENT
FROM @TECHCATALYST_DE.EXTERNAL_STAGE.AB_STAGE/songplays_table/ (FILE_FORMAT => 'TECHCATALYST_DE.EXTERNAL_STAGE.AB_PARQUET_FORMAT', PATTERN => '.*parquet.*');
```
