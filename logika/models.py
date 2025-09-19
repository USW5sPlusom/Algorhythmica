from django.db import models

class Bead(models.Model):
    text = models.TextField(verbose_name='Текст цитаты', help_text='Введите полный текст цитаты')
    philosopher_name = models.CharField(verbose_name='Автор цитаты', help_text='Введите автора цитаты', max_length=100)
    
    def __str__(self):
        return f'{self.philosopher_name}: "{self.text[:50]}..."'

    class Meta:
        verbose_name = 'бусина'
        verbose_name_plural = 'бусины'
        ordering = ['philosopher_name']