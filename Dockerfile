# FROM wallies/python-cuda:3.10-cuda11.6-runtime
FROM python:3.10.11

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
