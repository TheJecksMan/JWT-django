import datetime

from django.db import models
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User


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


class CommentsNews(models.Model):
    news = models.ForeignKey(NewsApp, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    comment = MDTextField('Комментарий')
    date = models.DateTimeField('Дата публикации', default=datetime.datetime.now)

    def __str__(self):
        return self.comment

    class Meta:

        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'
