FROM python:3.9-slim

ARG APP_DIR
WORKDIR /app

COPY containers/${APP_DIR}/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY containers/${APP_DIR} /app

CMD ["python", "app.py"]
