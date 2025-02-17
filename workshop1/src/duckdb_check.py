import duckdb

def extract_data():
    try:
        # Connect to the DuckDB database
        con = duckdb.connect('/home/saithihazaw/projects/dtc-data-engineering/workshop1/src/ny_taxi_pipeline.duckdb')
        print("Connected to DuckDB database.")

        # Check if the 'rides' table exists
        tables = con.execute("SHOW TABLES").fetchall()
        print("Tables in the database:", tables)
        if ('rides',) in tables:
            print("'rides' table exists. Querying data...")
            # Query the database
            result = con.execute('SELECT * FROM rides LIMIT 10').fetchall()
            print("Data in rides table:")
            for row in result:
                print(row)
        else:
            print("'rides' table does not exist. Please ensure data is inserted correctly.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == '__main__':
    extract_data()
