#!/usr/bin/env python

import pika
import sys
from pika.exceptions import ConnectionClosedByBroker as ConnectionClosed

def fib(n):
    if n == 0:
        return 0
    a = 1
    b = 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

def callback(ch, method, props, body):
    n = int(body)
    r = fib(n)
    print(" [.] fib(%d)=%d" % (n, r))
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
        body=str(r)
    )
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
        channel.queue_declare(queue='rpc_queue')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue='rpc_queue',
            on_message_callback=callback
        )
        print(" [*] Waiting RPC requests")
        channel.start_consuming()
    except KeyboardInterrupt as ki:
        print("User cancelled!")
    except ConnectionClosed as cc:
        print("Connection closed by broker!")

