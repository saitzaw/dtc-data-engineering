## python needs extra library for google 
```shell 
pip install google
pip install google-auth google-auth-oauthlib
pip install google-cloud-bigquery
pip install google-cloud-storage  
```

## Google cloud login 
gcloud auth application-default login 

## use the json file 
- download the json file or point the json file 

## Bucket 
- create new bucket or use the old bucket 


## check table size 
bq show --format=prettyjson gcp-terraform-sthz:nytaxi.stg_yellow_01 | grep "numBytes"

