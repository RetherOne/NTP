from django.db import models
from datetime import *

class bd(models.Model):
    title = models.CharField('Название', max_length=50)
    contents = models.TextField('Содержание', null=True, blank=True, max_length=300)
    datatime = models.DateTimeField(default=datetime.now)

    class Meta():
        verbose_name = 'Публикации'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
