from django.db import models

class Bead(models.Model):
    text = models.TextField(verbose_name='Текст цитаты', help_text='Введите полный текст цитаты')
