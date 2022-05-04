from rest_framework import serializers
from ..models import NewsApp


class ListNews(serializers.ModelSerializer):
    class Meta:
        model = NewsApp
        fields = ('id', 'date', 'tags', 'title', 'anons')


class GetNews(serializers.ModelSerializer):
    class Meta:
        model = NewsApp
        fields = '__all__'
