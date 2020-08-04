# Introduction

Tinker w/ RabbitMQ.

## Startup the environment

This project sets up a RabbitMQ environment using docker-compose.
So make sure you have docker and docker-compose install properly.

To bring up the environment you type:

    docker-compose up

under the top level directory of this project.

## labs

This project follows [the official rabbitmq tutorial][1] and contains exactly six
parts:

- Hello World
- Work queues
- Publish/Subscribe
- Routing
- Topics
- RPC

The following table lists the directory corresponding to each part.

|       Part         |        Directory         |
|--------------------|:-------------------------|
| Hello World        | labs/python/hello        |
| Work Queue         | labs/python/queue        |
| Publish/Subscribe  | labs/python/pub-sub      |
| Routing            | labs/python/routing      |
| Topics             | labs/python/topics       |
| RPC                | labs/python/rpc          |

To play with the python lab you should install the [pika library][2] as follows:

    cd labs/python
    pip install -r requirements.txt


### Hello World

### Work Queue

### Publish/Subscribe

### Routing

### Topics

### RPC

[1]: https://www.rabbitmq.com/getstarted.html
[2]: https://pypi.org/project/pika/
