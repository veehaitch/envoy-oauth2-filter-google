FROM python:3.9

RUN mkdir -p /app
COPY ./upstream.py /app

CMD ["python3", "/app/upstream.py", "--listen-port", "40081"]
