#!/usr/bin/env python

import pika
import sys

if __name__ == '__main__':
    message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            virtual_host='myvhost'
        )
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    channel.basic_publish(
        exchange='logs',
        routing_key='',
        body=message
    )
    print(" [x] Send 'message: %s!'" % message)
    connection.close()