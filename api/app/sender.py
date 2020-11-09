import json
import pika
from envparse import env
from .schemas import Task

username = env('RABBITMQ_DEFAULT_USER')
password = env('RABBITMQ_DEFAULT_PASS')

credentials = pika.PlainCredentials(username, password)

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='rabbitmq',
    credentials=credentials
))
channel = connection.channel()
channel.queue_declare(queue='tasks')

async def send_task(task: Task):
    channel.basic_publish(
        exchange='', 
        routing_key='tasks', 
        body=json.dumps(task.json())
    )
