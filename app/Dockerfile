# Official base image
FROM python:3.10

# Environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Working directory
WORKDIR /usr/src/app

# Install dependencies (system)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat \
    python3-dev

# Copy all files
COPY . /usr/src/app

# Install dependencies (python)
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

# Expose port
EXPOSE 8000