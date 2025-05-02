from time import sleep
from celery import Celery, shared_task
from random import randint
from calc.models import Processamento

#app = Celery('task', broker='amqp://localhost:5672')

@shared_task
def processar_numeros(id):
    p = Processamento.objects.get(id=id)
    nums = sorted([p.num1, p.num2, p.num3])
    p.media = sum(nums) / 3
    p.mediana = nums[1]
    p.status = "Concluído"
    p.save()
