# Introduction

Tinker w/ RabbitMQ.

## Startup the environment

This project sets up a RabbitMQ environment using docker-compose.
So make sure you have docker and docker-compose install properly.

To bring up the environment you type:

    docker-compose up

under the top level directory of this project.

This environment include a RabbitMQ broker and an management node.
To access the RabbitMQ broker, you may attach to the docker container
by typing:

    docker exec -it rabbit01 /bin/bash

To access the admin webui, you open a web browser and navigate to [http://localhost:8001][3].

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

Open 2 consoles, in the first console, run the receiver as follows:

    cd labs/python/hello
    python receive.py

In the second console, run the sender as follows:

    cd labs/python/hello
    python send.py


### Work Queue

Open 2 or more consoles and run the following command in each console:

    cd labs/python/queue
    python worker.py

Then generates task to do as follows:

    cd labs/python/queue
    python new-task.py First message.
    python new-task.py Second message..
    python new-task.py Third message...
    python new-task.py Forth message....
    python new-task.py Fifth message.....
    python new-task.py Sixth message......
    python new-task.py Seventh message.......
    python new-task.py Eighth message........
    python new-task.py Nineth message.........

### Publish/Subscribe

### Routing

### Topics

### RPC

[1]: https://www.rabbitmq.com/getstarted.html
[2]: https://pypi.org/project/pika/
[3]: http://localhost:8001/
