from celery import Celery, shared_task

app = Celery('task', broker='amqp://localhost:5672')


@app.task(name='calc.task.hello')
def hello(nome:str):
    print('Hello {}'.format(nome))
    return 'Hello, World!'