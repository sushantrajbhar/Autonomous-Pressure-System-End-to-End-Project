# Use Python 3.8.5 slim-buster as the base image
FROM python:3.8.5-slim-buster

# Update package list, install awscli and required build tools
RUN apt update -y && \
    apt install -y awscli gcc build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app

# Command to run the application
CMD ["python3", "main.py"]
