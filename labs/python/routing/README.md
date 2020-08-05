# Introduction

Explore rabbitmq routing.

## test instruction

Open four consoles and run the following command in each console:

    python receive-log-direct.py info
    python receive-log-direct.py warn
    python receive-log-direct.py error
    python receive-log-direct.py info warn error

Then emit logs as follows:

    python emit-log-direct.py info good to see you
    python emit-log-direct.py info hi
    python emit-log-direct.py info bye
    python emit-log-direct.py warn fire
    python emit-log-direct.py error opos
