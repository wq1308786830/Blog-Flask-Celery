#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


"""
1.Run this in command line:
    celery -A celerys worker --pool=solo -l inf
    
2.Run these in python client:
    from tasks import add
    result = add.delay(4,4)
    result.ready()
    Out[4]: True
    result.get(timeout=1)
    Out[5]: 8
    result.get(propagate=False)
    Out[6]: 8
    result.traceback
    
Any problem, read these doc:
    http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celerys.html#redis
    http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#broker-redis
    
"""
