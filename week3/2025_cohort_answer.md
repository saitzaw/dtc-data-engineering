## prepare dataset
```SQL 
CREATE VIEW nytaxi.m_yellow_taxi AS
SELECT * FROM nytaxi.stg_yellow_01
UNION ALL
SELECT * FROM nytaxi.stg_yellow_02
UNION ALL
SELECT * FROM nytaxi.stg_yellow_03
UNION ALL
SELECT * FROM nytaxi.stg_yellow_04
UNION ALL
SELECT * FROM nytaxi.stg_yellow_05
UNION ALL
SELECT * FROM nytaxi.stg_yellow_06;
```

Q1. SELECT count(*) FROM `gcp-terraform-sthz.nytaxi.m_yellow_taxi` 
0,332,093 

Q2. 
```SQL
CREATE MATERIALIZED VIEW nytaxi.mv_yellow_taxi AS
SELECT * FROM nytaxi.stg_m_yellow_01
UNION ALL
SELECT * FROM nytaxi.stg_m_yellow_02
UNION ALL
SELECT * FROM nytaxi.stg_m_yellow_03
UNION ALL
SELECT * FROM nytaxi.stg_m_yellow_04
UNION ALL
SELECT * FROM nytaxi.stg_m_yellow_05
UNION ALL
SELECT * FROM nytaxi.stg_m_yellow_06;
```

gcp-terraform-sthz-demo-bucket-1111

```SQL
CREATE OR REPLACE EXTERNAL TABLE `nytaxi.external_yellow_taxi`
OPTIONS (
  format = 'parquet',
  uris = ['gs://gcp-terraform-sthz-demo-bucket-1111/yellow_tripdata_2024-*.parquet']
);
```

```SQL 
SELECT COUNT(DISTINCT PULocationID) FROM `gcp-terraform-sthz.nytaxi.stg_m_yellow_01` 
SELECT COUNT(DISTINCT PULocationID) FROM `gcp-terraform-sthz.nytaxi.stg_m_yellow_02` 
SELECT COUNT(DISTINCT PULocationID) FROM `gcp-terraform-sthz.nytaxi.stg_m_yellow_03` 
SELECT COUNT(DISTINCT PULocationID) FROM `gcp-terraform-sthz.nytaxi.stg_m_yellow_04` 
SELECT COUNT(DISTINCT PULocationID) FROM `gcp-terraform-sthz.nytaxi.stg_m_yellow_05` 
SELECT COUNT(DISTINCT PULocationID) FROM `gcp-terraform-sthz.nytaxi.stg_m_yellow_06` 
```
0 and 0 

Q3. 

```SQL 
SELECT 
    PULocationID
    , DOLocationID
FROM 
    `nytaxi.mv_yellow_taxi`
```
BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

Q4. 
```SQL 
SELECT 
    count(*)
FROM 
    `nytaxi.mv_yellow_taxi` where fare_amount = 0; 
```
8333

Q5. 
```SQL 
CREATE TABLE nytaxi.optimized_table
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT *
FROM nytaxi.mv_yellow_taxi;
```
Partitioning: Reduces the amount of data scanned by the query when filtering by the tpep_dropoff_datetime column.

Clustering: Organizes the data within each partition to improve the performance of queries that sort or filter by the VendorID column.

Q6. 
```SQL 
SELECT DISTINCT VendorID
FROM nytaxi.mv_yellow_taxi
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15';
```
```SQL 
select 
  sum(size_bytes)/pow(10,9) as sizeGB
from
  `nytaxi.__TABLES__`
where 
  table_id = 'mv_yellow_taxi';
```

```SQL 
select 
  sum(size_bytes)/pow(10,9) as sizeGB
from
  `nytaxi.__TABLES__`
where 
  table_id = 'optimized_table';
```

```SQL 
CREATE OR REPLACE TABLE nytaxi.yellow_taxi_partitioned
PARTITION BY
  DATE(tpep_dropoff_datetime) AS
SELECT * FROM nytaxi.external_yellow_taxi;
```
5.87 MB for non-partitioned table and 0 MB for the partitioned table

Q7. 
GCP bucket 

Q8. 
False 

Q9. 
```SQL
SELECT COUNT(*)
FROM nytaxi.mv_yellow_taxi;

```
shuffle 459 B 
0Byte 