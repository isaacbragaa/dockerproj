FROM python:3.9


WORKDIR /app


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY containers /app/


ARG APP_DIR
WORKDIR /app/${APP_DIR}


CMD ["python", "app.py"]
