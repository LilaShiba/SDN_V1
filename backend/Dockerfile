# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install system dependencies if required (e.g., libzmq, zlib)
RUN apt-get update && apt-get install -y \
    libzmq3-dev \
    zlib1g-dev \
    libffi-dev \
    libbz2-dev \
    liblzma-dev \
    libsqlite3-dev \
    tk-dev \
    libssl-dev

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the FLASK_APP environment variable to point to your application
ENV FLASK_APP=app/app.py

# Expose the port the app runs on (8008 in this case)
EXPOSE 8008

# Run the Flask application on port 8008
CMD ["flask", "run", "--host=0.0.0.0", "--port=8008"]
