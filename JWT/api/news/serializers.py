from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import NewsApp, CommentsNews


class ListNews(serializers.ModelSerializer):
    class Meta:
        model = NewsApp
        fields = ('id', 'date', 'tags', 'title', 'anons')

    def to_representation(self, instance):
        return change_json(super().to_representation(instance))


class GetNews(serializers.ModelSerializer):
    class Meta:
        model = NewsApp
        fields = '__all__'

    def to_representation(self, instance):
        return change_json(super().to_representation(instance))


class SetComment(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=500)
    news_id = serializers.IntegerField(required=True)


class GetComments(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)

    class Meta:
        model = CommentsNews
        fields = ('id', 'user', 'comment', 'date')


def change_json(result):
    # Изменение формата даты
    date = datetime.strptime(result['date'], '%Y-%m-%d')
    result['date'] = date.strftime("%A, %B %d, %Y")
    # Получение тегов в массив
    result['tags'] = result['tags'].split(', ')
    return result
