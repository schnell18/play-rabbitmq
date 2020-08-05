#!/usr/bin/env python

import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" %body)

if __name__ == '__main__':
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost',
                virtual_host='myvhost'
            )
        )
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_consume(
            queue='hello',
            auto_ack=True,
            on_message_callback=callback
        )
        print(" [*] Waiting for messages. Press CTRL+C to exit")
        channel.start_consuming()
    except KeyboardInterrupt as ki:
        print("User cancelled!")
    except ConnectionClosed as cc:
        print("Connection closed by broker!")