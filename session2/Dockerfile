FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY ./app ./app

# Expose port
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]