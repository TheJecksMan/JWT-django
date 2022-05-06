from datetime import datetime
from rest_framework import serializers
from ..models import NewsApp


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


def change_json(result):
    # Изменение формата даты
    date = datetime.strptime(result['date'], '%Y-%m-%d')
    result['date'] = date.strftime("%A, %B %d, %Y")
    # Получение тегов в массив
    result['tags'] = result['tags'].split(', ')
    return result
