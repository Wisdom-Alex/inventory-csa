FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    INVENTORY_DB=/data/inventory.db

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY inventory_app ./inventory_app
COPY data ./data
RUN mkdir -p /data

EXPOSE 8000

# Migrate legacy JSON into SQLite (idempotent), then start the API.
CMD ["sh", "-c", "python -m inventory_app.migrate && uvicorn inventory_app.api:app --host 0.0.0.0 --port 8000"]
