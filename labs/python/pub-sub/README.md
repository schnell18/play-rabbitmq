# Introduction

Explore rabbitmq fanout.

## test instruction

Open four consoles and run the following command in each console:

    python receive-log.py
    python receive-log.py
    python receive-log.py
    python receive-log.py

Then emit logs as follows:

    python emit-log.py info good to see you
    python emit-log.py info hi
    python emit-log.py info bye
    python emit-log.py warn fire
    python emit-log.py error opos
