from dataclasses import fields
from django.forms import IntegerField
from pkg_resources import require
from rest_framework import serializers
from ..models import News

from django.core.paginator import Paginator


class ListNews(serializers.Serializer):
    page = IntegerField(required=True)

    def update(self):
        page_num = self.validated_data['page']
        base_news = News.objects.order_by('date').reverse()
        p = Paginator(base_news, 5)
        count_list = p.page_range
        page = p.get_page(page_num)
        return base_news

    class Meta:
        model = News
        fields = ('__all__')
