from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Contatos(models.Model):

    OPERADORA_CHOICES = ((1, u'Vivo'),
                         (2, u'Tim'))

    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=100)
    operadora = models.CharField(max_length=2, choices=OPERADORA_CHOICES)

    class Meta:
        verbose_name = u"Contato"
