from django.db import models
from mdeditor.fields import MDTextField


class NewsApp(models.Model):
    title = models.CharField('Название', max_length=150)
    tags = models.CharField('Теги', max_length=150, help_text='Указывать через запятую')
    anons = models.TextField('Анонс')
    full_text = MDTextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
