from time import sleep
from celery import shared_task
from calc.models import Processamento

@shared_task
def processar_numeros(id):
    try:
        p = Processamento.objects.get(id=id)

        nums = sorted([p.num1, p.num2, p.num3])
        p.media = sum(nums) / 3
        p.mediana = nums[1]

        p.status = "Concluído"

        sleep(3) # Simulate a long-running task

        p.save()
        
    except Processamento.DoesNotExist:
        print(f"Registro com ID {id} não encontrado.")
        