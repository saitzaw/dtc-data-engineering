## Configuration and installation 
1. install wsl with Ubuntu 
2. install Docker in wsl [with Docker Desktop]
3. install gcloud in wsl 
4. install terrafrom 
5. open Google cloud provider account 


# Docker 
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

## 
## Run the script 
```shell 
docker run -it test:python3.9 2012-12-12
```

## Google cloud login 
gcloud auth application-default login 


## using Google keys file [Not recommended]
using export 

## terraform command 
terraform init 
terraform plan 
terraform apply
terraform destory