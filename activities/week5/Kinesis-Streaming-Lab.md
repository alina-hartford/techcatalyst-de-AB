# Discussion Points

## Diagram
![streaming_diagram](https://github.com/user-attachments/assets/7fd2ef53-cd4e-492c-ba1d-182d34c2c728)

## Discussion

1. Real-Time Data Streaming Concepts

2. Comparing Stream Processing Frameworks

3. AWS Kinesis

**4. Data Processing with Pyspark**
* You can import Window functions from the Pyspark.sql library and so the functions are used in the same way they are in sql. Window functions can be used to process streaming data by defining a window or time range in the data to perform aggregations on a small set of the data, rather than the entire stream.
* There is the pyspark.streaming module that has functions for reading, and controlling a data stream and making transformations with the resulting data. Transformations include union, join, groupby, filter, window, and map. 

**5. Delta Lake and Data Storage**
* A Delta Lake is an open-source table format for data storage that supports ACID transactions, query optimizations, schema evolution, and data versioning. Data Lakes stores and process raw data in any size or format. This can get messy because there is no proper data versioning or schema evolution like Delta Lakes. Data Warehouses, however, can only handle structured and semi-structured data, which makes it a bit more limiting in comparison to Delta Lakes.
* Atomicity ensures that all data changes are recorded, which means every time new data is processed, Delta Lakes will read and store this data. Consistency ensures the data meets the database's predefined rules and constraints every time new data is read. Isolation just means that each new stream of data is read and processed individually. This ensures that the correct transformations are made, if any. Finally, durability ensures that once a data transaction is completed, it will be safe. Overall, Delta Lakes ensures data reliability of data streams.

**6. Partitioning Strategy**
* Due to the limit of the amount of data that can be stored on a single device, partitioning ensures the optimal use of storage.  And since data is constantly being streamed, there is a lot of data to work with. To easily store and read the data, partitioning ensures that each piece of data is securely stored and can be found. 
     * Some other partitioning strategies that can be used based on how the data is being used. You can partition the data by usage like customer purchases, compared to customer returns.
* Fine-grained partitioning takes less computation time than coarse-grained partitioning. Fine grain partitioning means that data is broken into large number of small data, while coarse-grained partitioning is when data is broken into small numbers of large data. 

7. Performance and Scalability

8. Error Handling and Monitoring

9. Use Cases and Applications
