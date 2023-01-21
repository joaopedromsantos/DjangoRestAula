from django.db import models
from uuid import uuid1

##banco do produto

class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1, editable=False)
    nome = models.CharField(max_length=45)
    marca = models.CharField(max_length=20)
    preco = models.FloatField()
    quantidade = models.IntegerField()
