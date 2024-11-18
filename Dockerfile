# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask pillow requests

# Expose the Flask app's port
EXPOSE 6000

# Run the Flask app
CMD ["python", "app.py"]
