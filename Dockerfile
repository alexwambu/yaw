FROM python:3.11-slim

WORKDIR /app

# Install required packages including fonts for moviepy TextClip
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libgl1 \
    libglib2.0-0 \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Copy app code
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ensure storage directory exists
RUN mkdir -p /app/storage

EXPOSE 8501

# Streamlit entry point
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

