FROM python:3.10-slim

WORKDIR /app

# Install dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 5000

# Use array syntax for CMD
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
