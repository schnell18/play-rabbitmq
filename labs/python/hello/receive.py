#!/usr/bin/env python

import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" %body)

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=callback
    )
    print(" [*] Waiting for messages. Press CTRL+C to exit")
    channel.start_consuming()