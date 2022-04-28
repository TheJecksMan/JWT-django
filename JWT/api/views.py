from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.response import Response
from rest_framework import status

from . import serializers


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def login_account(request):
    """
    Получение данных, при входе в аккаунт
    """
    user = request.user
    return Response({
        'username': user.username,
        'firstname': user.first_name,
        'lastname': user.last_name,
        'date_joined': user.date_joined.strftime("%d.%m.%Y %H:%M"),
    })


@ api_view(['POST'])
def regustration_account(request):
    """
    Регистрация нового пользователя
    """
    serializer = serializers.RegistartionAccount(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        if user:
            return Response(status=status.HTTP_200_OK)

    return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
