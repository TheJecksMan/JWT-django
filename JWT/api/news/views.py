from .serializers import ListNews, GetNews, SetComment, GetComments
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from ..models import CommentsNews, NewsApp

from django.contrib.auth.models import User

from ..models import NewsApp
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ListNews(ListAPIView):
    """Получение списка с использование пагинатора. 
    Максимально 5 объектов
    """
    queryset = NewsApp.objects.order_by('id').reverse()
    serializer_class = ListNews
    pagination_class = PageNumberPagination


class Post(ListAPIView):
    """Получение подробной информации о конкретной новости
    """
    queryset = NewsApp.objects.all()
    serializer_class = GetNews

    def get(self, request, *args, **kwargs):
        id = request.query_params['id']

        if id == "" or not NewsApp.objects.filter(pk=id):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        news = NewsApp.objects.get(pk=id)
        serializer = GetNews(news)
        return Response(serializer.data)


class Comments(ListAPIView):
    """Получение комментариев к новости
    """
    queryset = CommentsNews.objects.all()
    serializer_class = GetComments
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['news']
    ordering_fields = ['date']
    pagination_class = PageNumberPagination


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request: Request):
    serializer = SetComment(data=request.data)
    if serializer.is_valid():
        user_id = request.user.id
        result = CommentsNews.objects.create(
            news=NewsApp(id=serializer.validated_data['news_id']),
            user=User(id=user_id),
            comment=serializer.validated_data['text'],
        )
        result.save()
        return Response({"detail": "ok"})
    else:
        return Response({
            'detail': serializer._errors}, status=status.HTTP_400_BAD_REQUEST
        )
