# Use Python as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variable for Django settings module
ENV DJANGO_SETTINGS_MODULE=config.settings

# Copy project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port for Django
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
