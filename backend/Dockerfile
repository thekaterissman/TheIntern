# Stage 1: The Build Stage - Install dependencies
FROM python:3.11-slim as builder

WORKDIR /app

# Copy and install dependencies first to leverage Docker's build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the core application code
COPY ./backend/server.py .
COPY ./frontend/index.html .

# Stage 2: The Production Stage - Super lightweight runtime
FROM python:3.11-slim
WORKDIR /app

# Copy only the necessary runtime files from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY --from=builder /app .

# Expose the application port
EXPOSE 8080

# The command to run the Living Aura server (The Intern App)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "server:app"] 
