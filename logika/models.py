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
        

class Thread(models.Model):
    """
    Нить — контейнер для набора нанизанных бусин (ThreadNode).
    Пока содержит метаданные: имя, описание, флаги и таймстемпы.
    Реальная логика присвоения символов будет реализована после добавления ThreadNode.
    """
    name = models.CharField(help_text='Имя', blank=True, max_length=200)
    description = models.TextField(help_text='Описание', blank=True)
    is_active = models.BooleanField(help_text='Флаг активнности нити', default=True)
    