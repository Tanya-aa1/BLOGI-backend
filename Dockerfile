# Use the official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy wait-for-it.sh script (make sure it exists in your project root)
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Copy the rest of the app code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Use wait-for-it to delay FastAPI startup until Postgres is ready
CMD ["./wait-for-it.sh", "db:5432", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]