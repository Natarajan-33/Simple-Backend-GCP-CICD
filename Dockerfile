# Use a minimal official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Set default port for Cloud Run but allow override
ENV PORT=8080

# Expose the default port
EXPOSE ${PORT}

# Print the port being used (optional but useful for debugging)
# And run the app using the dynamic PORT
CMD echo "Starting server on port ${PORT}" && \
    uvicorn main:app --host 0.0.0.0 --port ${PORT}
