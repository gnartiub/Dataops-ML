# Use the official Python image as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install curl
RUN apt-get update && apt-get install -y curl

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy the poetry.lock and pyproject.toml files into the container
COPY poetry.lock pyproject.toml ./

# Install dependencies using Poetry
RUN poetry install

# Copy the Flask application code into the container
COPY . .

# Expose port 5000 for Flask app
EXPOSE 5000

# Command to run the Flask application
CMD ["poetry", "run","python", "main.py"]
