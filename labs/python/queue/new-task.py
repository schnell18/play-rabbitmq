#!/usr/bin/env python

import pika
import sys

if __name__ == '__main__':
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode = 2 # make message persistent
        )
    )
    print(" [x] Send 'message: %s!'" % message)
    connection.close()