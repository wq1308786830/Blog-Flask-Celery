#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')
app.conf.broker_transport_options = {'visibility_timeout': 3600, 'fanout_prefix': True,
                                     'fanout_patterns': True}  # 1 hour.
app.conf.result_backend = 'redis://localhost:6379/0'

app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)

if __name__ == '__mian__':
    app.start()
