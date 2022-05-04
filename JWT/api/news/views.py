from django import views

from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.core.paginator import Paginator


@ api_view(['POST'])
def list_news(request):
    serializer = serializers.ListNews(data=request.data)
    if serializer.is_valid():
        serializer.update()
        return Response(serializer.data)
    else:
        return Response("Ошибка")
