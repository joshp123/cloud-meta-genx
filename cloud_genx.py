# cloud_genx_app thing
# this is where the parallel magic happens
# this module defines our tasks


from celery import Celery

app = Celery('hello', broker='amqp://guest@localhost//')

@app.task
def hello():
    return 'hello world'