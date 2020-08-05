#!/usr/bin/env python

import pika
import sys

if __name__ == '__main__':
    severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
    message = ' '.join(sys.argv[2:]) or "Hello World!"
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host='localhost',
            virtual_host='myvhost'
        )
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
    channel.basic_publish(
        exchange='direct_logs',
        routing_key=severity,
        body=message
    )
    print(" [x] Sent %r: %r!'" % (severity, message))
    connection.close()