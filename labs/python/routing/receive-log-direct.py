#!/usr/bin/env python

import pika
import sys
from pika.exceptions import ConnectionClosedByBroker as ConnectionClosed

def callback(ch, method, properties, body):
    print(" [x] %r: %r" % (method.routing_key, body))

if __name__ == '__main__':
    try:
        severities = sys.argv[1:]
        if not severities:
            sys.stderr.write("Usage: %s [info] [warn] [error]\n" % sys.argv[0])
            sys.exit(1)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost',
                virtual_host='myvhost'
            )
        )
        channel = connection.channel()
        channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        for severity in severities:
            channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

        channel.basic_consume(
            queue=queue_name,
            auto_ack=True,
            on_message_callback=callback
        )
        print(" [*] Waiting for %r logs. Press CTRL+C to exit" % severities)
        channel.start_consuming()
    except KeyboardInterrupt as ki:
        print("User cancelled!")
    except ConnectionClosed as cc:
        print("Connection closed by broker!")

