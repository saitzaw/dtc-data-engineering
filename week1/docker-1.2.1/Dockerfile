# Use an official Python runtime as a parent image
FROM python:3.12.8

# Install the required dependencies
RUN pip install pandas 

# Working directory
WORKDIR /app 

# Copy the current directory contents into the container at /app
COPY pipeline.py pipeline.py

# Run app.py when the container launches
ENTRYPOINT [ "python", "pipeline.py" ]
