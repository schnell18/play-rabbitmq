# Introduction

Explore rabbitmq routing.

## test instruction

Open four consoles and run the following command in each console:

    python receive-logs-topic.py '#'
    python receive-logs-topic.py 'kern.*
    python receive-logs-topic.py '*.critical'
    python receive-logs-topic.py 'kern.* '*.critical'

Then emit logs as follows:

    python emit-log-topic.py "kern.critical" "A critical kernel panic"
    python emit-log-topic.py "anon.critical" "A fake kernel panic"
    python emit-log-topic.py "kern.info" "A real kernel notice"
    python emit-log-topic.py "anon.warn" "A real annoying notice"
