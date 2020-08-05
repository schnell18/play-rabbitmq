#!/usr/bin/env python

import pika
import sys
import uuid

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost',
                virtual_host='myvhost'
            )
        )
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            body=str(n),
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
            )
        )

        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)

    def __del__(self):
        if self.connection:
            self.connection.close()

if __name__ == '__main__':
    arrays = []
    if len(sys.argv) < 2:
        arrays.append(10)
    for a in sys.argv[1:] :
        arrays.append(int(a))
    fib_client = FibonacciRpcClient()

    for n in arrays:
        print(" [x] Requesting fib(%d)" % n)
        response = fib_client.call(n)
        print(" [x] fib(%d)=%s " % (n, response))