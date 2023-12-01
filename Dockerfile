# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the requests module
RUN pip install requests

# Run ass4-main.py when the container launches
CMD ["python", "ass4-main.py"]
