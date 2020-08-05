# Introduction

Explore rabbitmq routing.

## test instruction

Open 2 or more console and run the following command in each console:

    python receive-logs-direct.py info warn error

Then emit logs as follows:

    python emit-log-direct.py info good to see you
    python emit-log-direct.py info hi
    python emit-log-direct.py info bye
    python emit-log-direct.py warn fire
    python emit-log-direct.py error opos
