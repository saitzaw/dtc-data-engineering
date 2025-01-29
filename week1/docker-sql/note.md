## docker network 
docker network create pg-network

## PGCLI 
pgcli -h 172.22.0.2 -p 5432 -u root -d ny_taxi

## Postgresql
```shell
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5433:5432 \
  --network pg-network \
  --name pg-database \
  postgres:13
```

## PgAdmin 
```shell
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin-2 \
  dpage/pgadmin4
```


## python 
### Build image
```shell
FROM python:3.12.8

# Install the required dependencies
RUN pip install pandas

# Working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY pipeline.py pipeline.py

# Run app.py when the container launches
ENTRYPOINT [ "python", "pipeline.py" ]
``` 
```shell 
docker build -t test:python3.9 . 
```
## Run the script 
```shell 
docker run -it test:python3.9 2012-12-12
```

## docker-compose
```shell 
services:
  pgdatabase:
    image: postgres:13
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=ny_taxi
    volumes:
      - "./ny_taxi_postgres_data:/var/lib/postgresql/data:rw"
      - "./pg_hba.conf:/var/lib/postgresql/data/pg_hba.conf:ro"
    ports:
      - "5433:5432"
    networks:
      - ny_taxi_network

  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    ports:
      - "8080:80"
    depends_on:
      - pgdatabase
    networks:
      - ny_taxi_network

networks:
  ny_taxi_network:
    driver: bridge
```

## Note 
- for Linux locally installed with postgresql, we I to change the port 5432 to 5433 or another number
- postgresql cannot connect with PgAdmin (docker) in docker  [WSL with windows]
- use the DBeaver instead of PgAdmin4 


## green trip data 
python ingest_data.py --user root --password root --host localhost --port 5432 --db ny_taxi --table_name yellow_taxi_data --url wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz

## zones data 
python ingest_data.py --user root --password root --host localhost --port 5432 --db ny_taxi --table_name yellow_taxi_data --url wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz


## 
```SQL
SELECT
    lpep_pickup_datetime,
    lpep_dropoff_datetime,
    total_amount,
    "PULocationID",
    "DOLocationID"
FROM 
    green_trip_data t
LEFT JOIN zones z1 ON t."PULocationID" = z1."LocationID"
LEFT JOIN zones z2 ON t."DOLocationID" = z2."LocationID"
WHERE z1."LocationID" IS NOT NULL 
OR z2."LocationID" is not null; 
```

```shell
total_count=476387
between_two_dates=476354
```

Q1, python 3.12.8 -> pip version  24.3.1

Q2, 
```Shell 
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin  

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```

that pgadmin should use to connect to the postgres database?
A2: postgres, 5433

Q3 ,
```SQL
SELECT
    SUM(CASE WHEN trip_distance <= 1 THEN 1 ELSE 0 END) AS up_to_1_mile,
    SUM(CASE WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1 ELSE 0 END) AS between_1_and_3_miles,
    SUM(CASE WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1 ELSE 0 END) AS between_3_and_7_miles,
    SUM(CASE WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1 ELSE 0 END) AS between_7_and_10_miles,
    SUM(CASE WHEN trip_distance > 10 THEN 1 ELSE 0 END) AS over_10_miles
FROM 
    green_trip_data 
WHERE
    lpep_pickup_datetime >= '2019-10-01' 
    AND lpep_pickup_datetime < '2019-11-01';
```
104830,198995,109642,27686,35201 -> 
A3, 104,838; 199,013; 109,645; 27,688; 35,202


Q4, 
```SQL 
SELECT
    DATE(lpep_pickup_datetime) AS pickup_date,
    MAX(trip_distance) AS max_trip_distance
FROM
    green_trip_data
WHERE
    lpep_pickup_datetime >= '2019-10-01'
    AND lpep_pickup_datetime < '2019-11-01'
GROUP BY
    pickup_date
ORDER BY
    max_trip_distance DESC
LIMIT 1;
```
A4 2019-10-31

Q5, 
```SQL
SELECT
    z."Zone",
    SUM(t.total_amount) AS total_amount
FROM
    green_trip_data t
JOIN
    zones z ON t."PULocationID" = z."LocationID"
WHERE
    DATE(t.lpep_pickup_datetime) = '2019-10-18'
GROUP BY
    z."Zone"
HAVING
    SUM(t.total_amount) > 13000
ORDER BY
    total_amount DESC;
```
A5 East Harlem North, East Harlem South, Morningside Heights