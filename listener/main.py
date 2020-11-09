import json, pika
from envparse import env

username = env('RABBITMQ_DEFAULT_USER')
password = env('RABBITMQ_DEFAULT_PASS')

credentials = pika.PlainCredentials(username, password)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq',
        credentials=credentials
    ))
    channel = connection.channel()
    channel.queue_declare(queue='tasks')

    def callback(channel, method, properties, body):
        task = json.loads(body.decode('utf8'))
        print(f"New task: {task}")

    channel.basic_consume(queue='tasks', on_message_callback=callback, auto_ack=True)

    print('Waiting for new tasks...')
    channel.start_consuming()

if __name__ == '__main__':
    main()