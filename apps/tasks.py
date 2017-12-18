# -*- coding: utf-8 -*-
# !/usr/bin/python
from celery import Celery


def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    task_base = celery.Task

    class ContextTask(task_base):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return task_base.__call__(self, *args, **kwargs)

    task_base = ContextTask

    @celery.task()
    def add_together(a, b):
        print('@celerys task add_together: ' + str(a + b))
        return a + b

    add_together(1, 2)

    return celery


app = Celery('hello', broker='redis://localhost:6379/0')


@app.task
def hello():
    return 'hello world'
