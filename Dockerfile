FROM python:3.11-slim

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY server.py .

ENV PORT=8242

CMD socat TCP-LISTEN:${PORT},reuseaddr,fork EXEC:"python3 /app/server.py",pty,stderr
