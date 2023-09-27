FROM python:3

WORKDIR /app

COPY server.py .

ENV PORT 10000

CMD ["python", "server.py"]