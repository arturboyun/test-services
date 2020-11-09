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

    def callback(ch, method, properties, body):
        message = json.loads(body.decode("UTF-8"))
        print(f"New task: {message}")

    channel.basic_consume(queue='tasks', on_message_callback=callback, auto_ack=True)

    print('Waiting for new tasks...')
    channel.start_consuming()

if __name__ == '__main__':
    main()