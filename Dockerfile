# Use an official Python runtime as a parent image

FROM python:3.9-slim
 
# Set the working directory

WORKDIR /app
 
# Copy the requirements file

COPY requirements.txt .
 
# Install dependencies

RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the application files

COPY . .
 
# Expose the port Flask runs on

EXPOSE 5000
 
# Set environment variables for Flask

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0
 
# Run the application

CMD ["flask", "run"]

