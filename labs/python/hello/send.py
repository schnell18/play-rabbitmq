#!/usr/bin/env python

import pika

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    for i in range(1, 10):
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body='[%02d] Hello World!' % i
        )
    print(" [x] Send 'Hello World!'")
    connection.close()