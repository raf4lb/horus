from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    '''
    Model of a contact entity
    '''
    owner = models.ForeignKey(User, on_delete=models.PROTECT,
                              related_name='contacts', verbose_name='Usuário')
    name = models.CharField(max_length=60, verbose_name='Nome')
    telephone = models.CharField(
        max_length=11, verbose_name='Telefone')
    deleted = models.BooleanField(default=False, verbose_name='Excluído')

    class Meta:
        unique_together = ('owner', 'telephone')

    def __str__(self):
        '''
        Default instance print
        '''
        return f'{self.name} {self.telephone}'
