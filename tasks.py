# Create your tasks here
from __future__ import absolute_import, unicode_literals

import time

from celery import Celery
from conf import settings

result_backend = settings['database_url']

app = Celery('hello', broker='amqp://guest@localhost//', result_backend=result_backend)


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def sleep(n):
    time.sleep(n)
    return n


@app.task
def testprint(p):
    print(p)
    return p
