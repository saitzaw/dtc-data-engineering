Q1. 
    128.3 MB

Q2.
    green_tripdata_2020-04.csv

Q3. 
        24,648,499
```SQL
SELECT COUNT(*) AS row_count 
FROM yellow_tripdata 
WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2020 
AND EXTRACT(MONTH FROM tpep_pickup_datetime) BETWEEN 1 AND 12;
```

Q4.
    1,734,051
```SQL
SELECT COUNT(*) AS row_count 
FROM green_tripdata gt
WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2020
AND EXTRACT(MONTH FROM lpep_pickup_datetime) between 1 and 12 ;
```

Q5. 
    1,925,152
```SQL
SELECT COUNT(*) AS row_count 
FROM yellow_tripdata 
WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2021
AND EXTRACT(MONTH FROM tpep_pickup_datetime) = 3; 
```

Q6.
    Add a timezone property set to America/New_York in the Schedule trigger configuration