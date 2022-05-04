from django.db import models


class News(models.Model):
    title = models.CharField('Название', max_length=150)
    tags = models.CharField('Теги', max_length=150, help_text='Указывать через запятую')
    anons = models.TextField('Анонс')
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
