FROM python:3.8-buster

COPY . /listener

WORKDIR /listener
RUN pip install -r requirements.txt

CMD ["python", "-u", "main.py"]
