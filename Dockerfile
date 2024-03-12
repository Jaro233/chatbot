# Use an official PyTorch base image
FROM bitnami/pytorch

WORKDIR /app

# Create a directory for the Transformers cache and ensure it's writable
RUN mkdir -p /app/transformers_cache && \
    chmod -R 777 /app/transformers_cache

# Set the TRANSFORMERS_CACHE environment variable
ENV TRANSFORMERS_CACHE=/app/transformers_cache

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application
COPY . /app

EXPOSE 80

CMD ["python", "app.py"]
