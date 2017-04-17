from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Tag(models.Model):

    nome = models.CharField(max_length=250)


    def __unicode__(self):
        return self.nome


class Contatos(models.Model):

    OPERADORA_CHOICES = ((1, u'Vivo'),
                         (2, u'Tim'))

    nome = models.CharField(max_length=250)
    telefone = models.CharField(max_length=100)
    operadora = models.CharField(max_length=2, choices=OPERADORA_CHOICES,
    	                         blank=True, null=True)
    tag = models.ManyToManyField(Tag, null=True, blank=True)

    class Meta:
        verbose_name = u"Contato"

    def get_absolute_url(self):
        return reverse('edit-contato', kwargs={'pk': self.pk})
