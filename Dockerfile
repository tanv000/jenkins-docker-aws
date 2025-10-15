# Dockerfile
# Use a minimal Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Command to run the Python script when the container starts
CMD ["python", "app.py"]
