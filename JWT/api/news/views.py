from .serializers import ListNews, GetNews
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from ..models import NewsApp
from rest_framework.pagination import PageNumberPagination


class ListNews(ListAPIView):
    """
    Получение списка с использование пагинатора. 
    Максимально 5 объектов
    """
    queryset = NewsApp.objects.order_by('id').reverse()
    serializer_class = ListNews
    pagination_class = PageNumberPagination


class Post(ListAPIView):
    """
    Получение подробной информации о конкретной новости
    """
    queryset = NewsApp.objects.all()
    serializer_class = GetNews

    def get(self, request, *args, **kwargs):
        id = request.query_params['id']

        if id is "" or not NewsApp.objects.filter(pk=id):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        news = NewsApp.objects.get(pk=id)
        serializer = GetNews(news)
        return Response(serializer.data)
