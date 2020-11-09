FROM python:3.8-buster

EXPOSE 80

COPY . /api

WORKDIR /api
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
