from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=150)
    anons = models.TextField('Анонс')
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    # news_id = models.OneToOneField(Articles.id, None)
    news = models.ForeignKey(
        Articles, on_delete=models.CASCADE, verbose_name='Новость')
    author = models.CharField('Автор', max_length=40)
    сomment_text = models.CharField('Комментарий', max_length=2000)
    date = models.DateTimeField('Опубликован')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
