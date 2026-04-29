FROM python:3.11-slim

WORKDIR /app
COPY server.py .

CMD ["python3", "/app/server.py"]
