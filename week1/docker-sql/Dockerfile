# Use an official Python runtime as a parent image
FROM python:3.12.8

# Install the required dependencies
RUN pip install pandas sqlalchemy psycopg2-binary

# Working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY pipeline.py pipeline.py

# Run app.py when the container launches
ENTRYPOINT [ "python", "pipeline.py" ]