# Introduction

Explore rabbitmq RPC.

## test instruction

Open three consoles and run the following command in each console:

    python rpc-server.py
    python rpc-server.py
    python rpc-server.py

Then request fibonacci calculation as follows:

    python rpc-client.py 0 1 2 3 4 5
    python rpc-client.py 10 20 30 40 50
    python rpc-client.py 100 200 300 400 500
    python rpc-client.py 1000 2000 3000 4000 5000
