#!/usr/bin/env python

import pika
import time

def callback(ch, method, properties, body):
    print(" [x] Received %r" %body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost',
                virtual_host='myvhost'
            )
        )
        channel = connection.channel()
        channel.queue_declare(queue='task_queue', durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue='task_queue',
            on_message_callback=callback
        )
        print(" [*] Waiting for messages. Press CTRL+C to exit")
        channel.start_consuming()
    except KeyboardInterrupt as ki:
        print("User cancelled!")
    except ConnectionClosed as cc:
        print("Connection closed by broker!")