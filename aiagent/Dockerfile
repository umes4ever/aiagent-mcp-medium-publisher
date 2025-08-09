FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY medium_aiagent ./medium_aiagent
COPY .env ./

EXPOSE 8000

CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]
