#!/usr/bin/env python

import pika
import sys
from pika.exceptions import ConnectionClosedByBroker as ConnectionClosed

def callback(ch, method, properties, body):
    print(" [x] %r: %r" % (method.routing_key, body))

if __name__ == '__main__':
    try:
        binding_keys = sys.argv[1:]
        if not binding_keys:
            sys.stderr.write("Usage: %s [binding_key] ... \n" % sys.argv[0])
            sys.exit(1)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost',
                virtual_host='myvhost'
            )
        )
        channel = connection.channel()
        channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        for binding_key in binding_keys:
            channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

        channel.basic_consume(
            queue=queue_name,
            auto_ack=True,
            on_message_callback=callback
        )
        print(" [*] Waiting for %r logs. Press CTRL+C to exit" % binding_keys)
        channel.start_consuming()
    except KeyboardInterrupt as ki:
        print("User cancelled!")
    except ConnectionClosed as cc:
        print("Connection closed by broker!")

