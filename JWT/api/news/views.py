from .serializers import ListNews
from rest_framework.generics import ListAPIView

from ..models import NewsApp
from rest_framework.pagination import PageNumberPagination


class ListNews(ListAPIView):
    queryset = NewsApp.objects.order_by('id').reverse()
    serializer_class = ListNews
    pagination_class = PageNumberPagination
