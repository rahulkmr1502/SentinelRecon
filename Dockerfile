FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY config.json .

RUN mkdir -p reports logs && \
    chmod 777 reports logs

CMD ["python", "src/main.py"]
