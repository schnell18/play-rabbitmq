#!/usr/bin/env python

import pika
import sys

if __name__ == '__main__':
    routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anon.info'
    message = ' '.join(sys.argv[2:]) or "Hello World!"
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            virtual_host='myvhost'
        )
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    channel.basic_publish(
        exchange='topic_logs',
        routing_key=routing_key,
        body=message
    )
    print(" [x] Sent %r: %r!'" % (routing_key, message))
    connection.close()