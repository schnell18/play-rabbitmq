#!/usr/bin/env python

import pika
from pika.exceptions import ConnectionClosedByBroker as ConnectionClosed

def callback(ch, method, properties, body):
    print(" [x] %r" %body)

if __name__ == '__main__':
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='logs', exchange_type='fanout')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='logs', queue=queue_name)
        channel.basic_consume(
            queue=queue_name,
            auto_ack=True,
            on_message_callback=callback
        )
        print(" [*] Waiting for logs. Press CTRL+C to exit")
        channel.start_consuming()
    except KeyboardInterrupt as ki:
        print("User cancelled!")
    except ConnectionClosed as cc:
        print("Connection closed by broker!")

