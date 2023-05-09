FROM python:3.9-slim-buster

RUN pip install boto3

WORKDIR /app

COPY randompython.py .

CMD ["python", "randompython.py"]
